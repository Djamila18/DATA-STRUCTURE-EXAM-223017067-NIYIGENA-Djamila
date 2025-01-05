# AVL Tree Implementation for Digital Coupons and Loyalty Program

class Node:
    def __init__(self, key, value):
        self.key = key  # Key could be CustomerID or CouponID
        self.value = value  # Value could be loyalty points, discount, etc.
        self.left = None
        self.right = None
        self.height = 1  # Height of the node to keep track of balance

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key, value):
        if not root:
            return Node(key, value)

        if key < root.key:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:  # Left Left case
            return self.rightRotate(root)
        if balance < -1 and key > root.right.key:  # Right Right case
            return self.leftRotate(root)
        if balance > 1 and key > root.left.key:  # Left Right case
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.key:  # Right Left case
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def insert_customer(self, key, value):
        self.root = self.insert(self.root, key, value)

    def search_customer(self, key):
        return self.search(self.root, key)

    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            print(f"CustomerID: {root.key}, Points: {root.value}")
            self.print_inorder(root.right)


# Stack Implementation to Track Actions (Undo feature)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, action):
        self.stack.append(action)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]


# Example Usage of AVL Tree and Stack in Digital Coupons and Loyalty Program

def main():
    # Instantiate the AVL tree and stack
    avl_tree = AVLTree()
    action_stack = Stack()

    # Add customers (example: customer ID and loyalty points)
    avl_tree.insert_customer(101, 500)  # Customer 101 with 500 points
    action_stack.push("Added Customer 101 with 500 points")

    avl_tree.insert_customer(102, 300)  # Customer 102 with 300 points
    action_stack.push("Added Customer 102 with 300 points")

    # Display all customers
    print("All customers:")
    avl_tree.print_inorder(avl_tree.root)

    # Search for a customer
    customer = avl_tree.search_customer(101)
    if customer:
        print(f"\nFound Customer 101 with points: {customer.value}")
    
    # Perform an undo action by popping from the stack
    last_action = action_stack.pop()
    print(f"\nUndo action: {last_action}")

    # Display the current stack status
    print(f"\nIs stack empty? {action_stack.is_empty()}")

    # Add another customer and perform undo
    avl_tree.insert_customer(103, 200)  # Customer 103 with 200 points
    action_stack.push("Added Customer 103 with 200 points")
    
    print("\nAll customers after adding customer 103:")
    avl_tree.print_inorder(avl_tree.root)
    
    last_action = action_stack.pop()
    print(f"\nUndo action: {last_action}")
    
    # Check the state of the stack
    print(f"\nIs stack empty? {action_stack.is_empty()}")


if __name__ == "__main__":
    main()
