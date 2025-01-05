class Node:
    def __init__(self, order_id, customer_id, coupon_id, loyalty_points_used, order_date):
        self.order_id = order_id  # Order ID
        self.customer_id = customer_id  # Customer ID
        self.coupon_id = coupon_id  # Coupon ID
        self.loyalty_points_used = loyalty_points_used  # Points used in the order
        self.order_date = order_date  # Date of the order
        self.next = None  # Link to the next node

class LinkedList:
    def __init__(self, max_orders):
        self.head = None  # Head of the linked list
        self.tail = None  # Tail of the linked list
        self.max_orders = max_orders  # Maximum number of orders
        self.size = 0  # Current size of the linked list

    def insert_order(self, order_id, customer_id, coupon_id, loyalty_points_used, order_date):
        """Insert a new order into the linked list."""
        if self.size == self.max_orders:
            self.remove_oldest_order()  # Remove the oldest order if the list is full

        new_node = Node(order_id, customer_id, coupon_id, loyalty_points_used, order_date)

        if self.size == 0:
            self.head = self.tail = new_node  # If the list is empty, the new node is both head and tail
        else:
            self.tail.next = new_node  # Add new order to the end of the list
            self.tail = new_node  # Update the tail

        self.size += 1
        print(f"Order {order_id} added for Customer {customer_id} using Coupon {coupon_id}.")

    def remove_oldest_order(self):
        """Remove the oldest order (the head of the list)."""
        if self.head:
            print(f"Removing oldest order: {self.head.order_id}")
            self.head = self.head.next  # Move the head pointer to the next node
            self.size -= 1
            if self.size == 0:
                self.tail = None  # If the list is now empty, set the tail to None

    def display_orders(self):
        """Display all orders in the linked list."""
        if not self.head:
            print("No orders in the system.")
            return

        current = self.head
        print("Orders in the system:")
        while current:
            print(f"OrderID: {current.order_id}, CustomerID: {current.customer_id}, CouponID: {current.coupon_id}, "
                  f"Points Used: {current.loyalty_points_used}, Order Date: {current.order_date}")
            current = current.next

    def search_order_by_id(self, order_id):
        """Search for an order by its OrderID."""
        current = self.head
        while current:
            if current.order_id == order_id:
                return current
            current = current.next
        return None

# Example Usage of LinkedList in the Digital Coupons and Loyalty Program

def main():
    # Set a maximum of 3 orders in the system at any time
    order_list = LinkedList(3)

    # Insert orders
    order_list.insert_order(101, 1001, 201, 150, "2025-01-01")
    order_list.insert_order(102, 1002, 202, 200, "2025-01-02")
    order_list.insert_order(103, 1003, 203, 250, "2025-01-03")

    # Display all orders
    order_list.display_orders()

    # Insert a new order when the list is full (it should remove the oldest order)
    order_list.insert_order(104, 1004, 204, 100, "2025-01-04")

    # Display orders after the list has been updated
    order_list.display_orders()

    # Search for a specific order by OrderID
    order = order_list.search_order_by_id(102)
    if order:
        print(f"\nOrder found: OrderID: {order.order_id}, CustomerID: {order.customer_id}")
    else:
        print("\nOrder not found.")

if __name__ == "__main__":
    main()

