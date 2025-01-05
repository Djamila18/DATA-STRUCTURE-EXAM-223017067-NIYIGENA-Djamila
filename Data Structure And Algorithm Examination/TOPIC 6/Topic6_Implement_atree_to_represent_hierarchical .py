class TreeNode:
    def __init__(self, id, data):
        self.id = id  # Unique identifier (could be CustomerID, CouponID, etc.)
        self.data = data  # Associated data (could be points, discount values, etc.)
        self.children = []  # List of child nodes

    def add_child(self, child_node):
        """Adds a child node to the current node."""
        self.children.append(child_node)

    def __repr__(self):
        """For easy printing of the node."""
        return f"TreeNode(ID: {self.id}, Data: {self.data})"


class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, root_node):
        """Set the root of the tree."""
        self.root = root_node

    def find_node(self, root, id):
        """Recursively searches for a node with a given ID."""
        if root is None:
            return None
        if root.id == id:
            return root
        for child in root.children:
            found_node = self.find_node(child, id)
            if found_node:
                return found_node
        return None

    def add_node(self, parent_id, new_node):
        """Adds a new node under the parent with given ID."""
        parent_node = self.find_node(self.root, parent_id)
        if parent_node:
            parent_node.add_child(new_node)
            print(f"Node with ID {new_node.id} added under parent ID {parent_id}.")
        else:
            print(f"Parent node with ID {parent_id} not found.")

    def display_tree(self, root, level=0):
        """Prints the tree structure in a readable format."""
        if root is None:
            return
        print(" " * level * 4 + f"{root.id}: {root.data}")
        for child in root.children:
            self.display_tree(child, level + 1)


# Example Usage of Tree Structure for Digital Coupons and Loyalty Program

def main():
    # Create the root of the tree (could represent a top-level entity, like the Loyalty Program)
    loyalty_program = Tree()
    root_node = TreeNode("Loyalty Program", "Main Program")  # This can be a root node for all customers
    loyalty_program.set_root(root_node)

    # Add some customers (Each customer is a child of the root node)
    customer1 = TreeNode("C1001", "Customer 1001, 500 Points")
    customer2 = TreeNode("C1002", "Customer 1002, 300 Points")
    loyalty_program.add_node("Loyalty Program", customer1)
    loyalty_program.add_node("Loyalty Program", customer2)

    # Add loyalty tiers (children of customers)
    silver_tier = TreeNode("Silver", "Silver Loyalty Tier")
    gold_tier = TreeNode("Gold", "Gold Loyalty Tier")
    loyalty_program.add_node("C1001", silver_tier)
    loyalty_program.add_node("C1002", gold_tier)

    # Add some coupons under each loyalty tier (can be child nodes of tiers)
    coupon1 = TreeNode("C201", "10% Discount Coupon")
    coupon2 = TreeNode("C202", "20% Discount Coupon")
    loyalty_program.add_node("Silver", coupon1)
    loyalty_program.add_node("Gold", coupon2)

    # Display the tree structure
    print("Tree Structure representing Loyalty Program:")
    loyalty_program.display_tree(loyalty_program.root)


if __name__ == "__main__":
    main()
