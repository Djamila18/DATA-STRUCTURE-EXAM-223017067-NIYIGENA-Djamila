class Coupon:
    def __init__(self, coupon_id, discount_percentage, priority):
        self.coupon_id = coupon_id
        self.discount_percentage = discount_percentage
        self.priority = priority  # Higher priority means more important coupon

    def __repr__(self):
        return f"Coupon({self.coupon_id}, {self.discount_percentage}%, Priority: {self.priority})"


class BucketSort:
    def __init__(self, num_buckets=10):
        self.num_buckets = num_buckets

    def bucket_sort(self, coupons, attribute='priority'):
        """Sort coupons using bucket sort based on the specified attribute (priority or discount)."""
        if attribute == 'priority':
            value_function = lambda coupon: coupon.priority
        elif attribute == 'discount_percentage':
            value_function = lambda coupon: coupon.discount_percentage
        else:
            raise ValueError("Unsupported attribute for sorting. Choose 'priority' or 'discount_percentage'.")

        # Step 1: Find the range (minimum and maximum values)
        min_value = min(coupons, key=value_function)
        max_value = max(coupons, key=value_function)

        # Calculate range for the bucket
        bucket_range = (value_function(max_value) - value_function(min_value)) / self.num_buckets

        # Step 2: Create empty buckets
        buckets = [[] for _ in range(self.num_buckets)]

        # Step 3: Place each coupon in its corresponding bucket
        for coupon in coupons:
            index = int((value_function(coupon) - value_function(min_value)) / bucket_range)
            if index == self.num_buckets:  # Edge case for the max value
                index -= 1
            buckets[index].append(coupon)

        # Step 4: Sort each bucket (we can use insertion sort or another algorithm)
        for i in range(self.num_buckets):
            buckets[i].sort(key=value_function, reverse=True)  # Sort within each bucket based on priority/discount

        # Step 5: Merge the buckets
        sorted_coupons = []
        for bucket in buckets:
            sorted_coupons.extend(bucket)

        return sorted_coupons


# Example Usage of Bucket Sort for Sorting Coupons by Priority or Discount

def main():
    # Sample coupons with ID, discount percentage, and priority
    coupons = [
        Coupon("C1001", 10, 3),
        Coupon("C1002", 25, 1),
        Coupon("C1003", 15, 2),
        Coupon("C1004", 50, 5),
        Coupon("C1005", 30, 4)
    ]

    print("Coupons before sorting:")
    for coupon in coupons:
        print(coupon)

    # Create an instance of BucketSort
    bucket_sorter = BucketSort(num_buckets=5)

    # Sort by priority
    sorted_coupons_by_priority = bucket_sorter.bucket_sort(coupons, attribute='priority')
    print("\nCoupons sorted by priority:")
    for coupon in sorted_coupons_by_priority:
        print(coupon)

    # Sort by discount percentage
    sorted_coupons_by_discount = bucket_sorter.bucket_sort(coupons, attribute='discount_percentage')
    print("\nCoupons sorted by discount percentage:")
    for coupon in sorted_coupons_by_discount:
        print(coupon)


if __name__ == "__main__":
    main()
