# Stack program
# Assessment 3.2: Stack Operations using TEOPIZ


# A stack removes the last letter added (LIFO)
class Stack:
    # Creates an empty stack
    def __init__(self):
        self.items = []

    # Adds a letter on top
    def push(self, data):
        self.items.append(data)

    # Removes and returns the top letter
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    # Returns True if the stack has no letters
    def is_empty(self):
        return len(self.items) == 0

    # Returns the stack as text
    def display(self):
        return "Bottom -> " + " ".join(self.items) + " <- Top"


# Pushes the letters of the name onto the stack, then pops them one by one
def run():
    print("\n--- Running Stack Program ---")
    default_name = "TEOPIZ"
    user_input = input(f"Enter your last name [Default: {default_name}]: ").strip().upper()
    name = user_input if user_input else default_name

    stack = Stack()

    # Push each letter
    print("\n--- Pushing letters ---")
    for letter in name:
        stack.push(letter)
        print("Pushed", letter, "->", stack.display())

    # Pop letters from the top
    print("\n--- Popping letters ---")
    while not stack.is_empty():
        removed = stack.pop()
        print("Popped", removed, "->", stack.display())

    print("\nThe stack is now empty.")


if __name__ == "__main__":
    run()