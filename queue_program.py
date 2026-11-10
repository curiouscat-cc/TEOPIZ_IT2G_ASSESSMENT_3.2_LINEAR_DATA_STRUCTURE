# Queue Program Implementation for TEOPIZ

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return "Front -> " + " ".join(self.items) + " <- Rear"

def run():
    name = "TEOPIZ"
    queue = Queue()

    print("\n--- Enqueuing letters ---")
    for letter in name:
        queue.enqueue(letter)
        print("Enqueued", letter, "->", queue.display())

    print("\n--- Dequeuing letters ---")
    while not queue.is_empty():
        removed = queue.dequeue()
        print("Dequeued", removed, "->", queue.display())

    print("\nThe queue is now empty.")

if __name__ == "__main__":
    run()