# Queue program
# Assessment 3.2: Queue Operations using TEOPIZ


# A queue removes the first letter added (FIFO)
class Queue:
    # Creates an empty queue
    def __init__(self):
        self.items = []

    # Adds a letter at the rear
    def enqueue(self, data):
        self.items.append(data)

    # Removes and returns the front letter
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    # Returns True if the queue has no letters
    def is_empty(self):
        return len(self.items) == 0

    # Returns the queue as text
    def display(self):
        return "Front -> " + " ".join(self.items) + " <- Rear"


# Enqueues the letters of the name, then dequeues them one by one
def run():
    print("\n--- Running Queue Program ---")
    default_name = "TEOPIZ"
    user_input = input(f"Enter your last name [Default: {default_name}]: ").strip().upper()
    name = user_input if user_input else default_name

    queue = Queue()

    # Enqueue each letter
    print("\n--- Enqueuing letters ---")
    for letter in name:
        queue.enqueue(letter)
        print("Enqueued", letter, "->", queue.display())

    # Dequeue letters from the front
    print("\n--- Dequeuing letters ---")
    while not queue.is_empty():
        removed = queue.dequeue()
        print("Dequeued", removed, "->", queue.display())

    print("\nThe queue is now empty.")


if __name__ == "__main__":
    run()