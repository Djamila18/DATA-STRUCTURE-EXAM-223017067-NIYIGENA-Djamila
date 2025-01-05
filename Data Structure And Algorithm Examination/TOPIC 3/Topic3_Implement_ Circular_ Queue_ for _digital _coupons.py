class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size of the queue
        self.queue = [None] * self.capacity  # The array holding the queue elements
        self.front = -1  # Front points to the first element of the queue
        self.rear = -1  # Rear points to the last element of the queue
        self.size = 0  # Track the current size of the queue
    
    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size == self.capacity
    
    def enqueue(self, customer_id, coupon_id, loyalty_points):
        """Add a new request (customer redemption or processing) to the queue."""
        if self.is_full():
            print("Queue is full! Cannot add more requests.")
            return
        
        # If queue is empty, set front and rear to the first element
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Circular increment of the rear index
            self.rear = (self.rear + 1) % self.capacity
        
        # Add customer redemption request to the queue
        self.queue[self.rear] = {'customer_id': customer_id, 'coupon_id': coupon_id, 'loyalty_points': loyalty_points}
        self.size += 1
        print(f"Enqueued: Customer {customer_id} redeemed Coupon {coupon_id} using {loyalty_points} points.")
    
    def dequeue(self):
        """Process (remove) the oldest request from the queue."""
        if self.is_empty():
            print("Queue is empty! No requests to process.")
            return None
        
        # Get the request at the front
        processed_request = self.queue[self.front]
        
        # If there's only one element, reset front and rear to -1
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            # Circular increment of the front index
            self.front = (self.front + 1) % self.capacity
        
        self.size -= 1
        print(f"Dequeued: Customer {processed_request['customer_id']} processed Coupon {processed_request['coupon_id']} redemption.")
        return processed_request
    
    def peek(self):
        """View the next request without removing it from the queue."""
        if self.is_empty():
            print("Queue is empty! No requests to peek.")
            return None
        return self.queue[self.front]
    
    def display(self):
        """Display the current state of the queue."""
        if self.is_empty():
            print("Queue is empty!")
            return
        index = self.front
        print("Current Queue:")
        while True:
            print(f"Customer {self.queue[index]['customer_id']} redeemed Coupon {self.queue[index]['coupon_id']} using {self.queue[index]['loyalty_points']} points.")
            if index == self.rear:
                break
            index = (index + 1) % self.capacity

# Example Usage of Circular Queue in a Digital Coupons and Loyalty Program

def main():
    # Instantiate the Circular Queue with a capacity of 5 requests
    cq = CircularQueue(5)
    
    # Enqueue some customer redemption requests (customer_id, coupon_id, loyalty_points)
    cq.enqueue(101, 201, 150)
    cq.enqueue(102, 202, 200)
    cq.enqueue(103, 203, 250)
    cq.enqueue(104, 204, 100)
    cq.enqueue(105, 205, 300)
    
    # Display the current state of the queue
    cq.display()
    
    # Dequeue (process) some requests
    cq.dequeue()  # Process the first request in the queue
    cq.dequeue()  # Process the next request in the queue
    
    # Display the queue after processing requests
    cq.display()
    
    # Enqueue more requests to demonstrate the circular nature
    cq.enqueue(106, 206, 400)
    cq.enqueue(107, 207, 500)
    
    # Display the final state of the queue
    cq.display()

if __name__ == "__main__":
    main()

