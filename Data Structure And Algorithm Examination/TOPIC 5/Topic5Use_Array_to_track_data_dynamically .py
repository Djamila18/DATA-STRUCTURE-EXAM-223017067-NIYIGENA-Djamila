class DigitalCouponLoyaltyProgram:
    def __init__(self):
        self.customers = []  # Array to store customer data
        self.orders = []  # Array to store order data
        self.coupons = []  # Array to store coupon data

    def add_customer(self, customer_id, loyalty_points):
        """Add a new customer to the loyalty program."""
        self.customers.append({'customer_id': customer_id, 'loyalty_points': loyalty_points})
        print(f"Customer {customer_id} added with {loyalty_points} loyalty points.")

    def add_order(self, order_id, customer_id, coupon_id, loyalty_points_used, order_date):
        """Add a new order and track coupon usage and loyalty points."""
        self.orders.append({'order_id': order_id, 'customer_id': customer_id,
                             'coupon_id': coupon_id, 'loyalty_points_used': loyalty_points_used,
                             'order_date': order_date})
        # Deduct the loyalty points used for the order from the customer's points
        for customer in self.customers:
            if customer['customer_id'] == customer_id:
                customer['loyalty_points'] -= loyalty_points_used
                break
        print(f"Order {order_id} added for Customer {customer_id} using Coupon {coupon_id}.")
        
    def add_coupon(self, coupon_id, discount_value, expiration_date):
        """Add a coupon to the system."""
        self.coupons.append({'coupon_id': coupon_id, 'discount_value': discount_value,
                              'expiration_date': expiration_date})
        print(f"Coupon {coupon_id} added with {discount_value}% discount, expires on {expiration_date}.")

    def display_customers(self):
        """Display all customers and their loyalty points."""
        if not self.customers:
            print("No customers in the system.")
        else:
            print("\nCustomers in the system:")
            for customer in self.customers:
                print(f"CustomerID: {customer['customer_id']}, Loyalty Points: {customer['loyalty_points']}")

    def display_orders(self):
        """Display all orders."""
        if not self.orders:
            print("No orders in the system.")
        else:
            print("\nOrders in the system:")
            for order in self.orders:
                print(f"OrderID: {order['order_id']}, CustomerID: {order['customer_id']}, "
                      f"CouponID: {order['coupon_id']}, Points Used: {order['loyalty_points_used']}, "
                      f"Order Date: {order['order_date']}")

    def display_coupons(self):
        """Display all available coupons."""
        if not self.coupons:
            print("No coupons in the system.")
        else:
            print("\nCoupons in the system:")
            for coupon in self.coupons:
                print(f"CouponID: {coupon['coupon_id']}, Discount: {coupon['discount_value']}%, Expiration Date: {coupon['expiration_date']}")

    def search_customer(self, customer_id):
        """Search for a customer by ID."""
        for customer in self.customers:
            if customer['customer_id'] == customer_id:
                return customer
        return None

    def search_coupon(self, coupon_id):
        """Search for a coupon by ID."""
        for coupon in self.coupons:
            if coupon['coupon_id'] == coupon_id:
                return coupon
        return None


# Example Usage of Array in Digital Coupons and Loyalty Program

def main():
    # Initialize the loyalty program
    program = DigitalCouponLoyaltyProgram()

    # Add customers
    program.add_customer(1001, 500)  # Customer 1001 with 500 points
    program.add_customer(1002, 300)  # Customer 1002 with 300 points

    # Add coupons
    program.add_coupon(201, 10, "2025-12-31")  # Coupon 201 with 10% discount
    program.add_coupon(202, 20, "2025-12-31")  # Coupon 202 with 20% discount

    # Add orders
    program.add_order(101, 1001, 201, 100, "2025-01-01")  # Order 101 by Customer 1001 using Coupon 201
    program.add_order(102, 1002, 202, 50, "2025-01-02")   # Order 102 by Customer 1002 using Coupon 202

    # Display customers, orders, and coupons
    program.display_customers()
    program.display_orders()
    program.display_coupons()

    # Search for a specific customer
    customer = program.search_customer(1001)
    if customer:
        print(f"\nFound Customer {customer['customer_id']} with {customer['loyalty_points']} loyalty points.")
    else:
        print("\nCustomer not found.")

    # Search for a specific coupon
    coupon = program.search_coupon(202)
    if coupon:
        print(f"\nFound Coupon {coupon['coupon_id']} with {coupon['discount_value']}% discount.")
    else:
        print("\nCoupon not found.")

if __name__ == "__main__":
    main()
