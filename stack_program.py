# Stack Program Implementation for TEOPIZ

class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return "Bottom -> " + " ".join(self.items) + " <- Top"

def run():
    name = "TEOPIZ"
    stack = Stack()

    print("\n--- Pushing letters ---")
    for letter in name:
        stack.push(letter)
        print("Pushed", letter, "->", stack.display())

    print("\n--- Popping letters ---")
    while not stack.is_empty():
        removed = stack.pop()
        print("Popped", removed, "->", stack.display())

    print("\nThe stack is now empty.")

if __name__ == "__main__":
    run()