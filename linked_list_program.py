# Linked list program
# Assessment 3.2: Singly Linked List Operations using TEOPIZ


# A node holds one letter and a link to the next node
class Node:
    # Creates a node with the given letter
    def __init__(self, data):
        self.data = data
        self.next = None


# A list of connected nodes
class LinkedList:
    # Creates an empty list
    def __init__(self):
        self.head = None
        self.tail = None

    # Adds a letter at the end of the list
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Removes and returns the first letter
    def remove(self):
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed

    # Returns True if the list has no nodes
    def is_empty(self):
        return self.head is None

    # Returns the list as text
    def display(self):
        current = self.head
        text = ""
        while current is not None:
            text += current.data + " -> "
            current = current.next
        return text + "NULL"


# Adds the letters of the name to the linked list, then removes them one by one
def run():
    print("\n--- Running Linked List Program ---")
    default_name = "TEOPIZ"
    user_input = input(f"Enter your last name [Default: {default_name}]: ").strip().upper()
    name = user_input if user_input else default_name

    linked_list = LinkedList()

    # Add each letter
    print("\n--- Adding letters ---")
    for letter in name:
        linked_list.add(letter)
        print("Added", letter, "->", linked_list.display())

    # Remove letters from the head
    print("\n--- Removing letters ---")
    while not linked_list.is_empty():
        removed = linked_list.remove()
        print("Removed", removed, "->", linked_list.display())

    print("\nThe linked list is now empty.")


if __name__ == "__main__":
    run()