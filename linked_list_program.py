# Singly Linked List Program Implementation for TEOPIZ

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        if self.head is None:
            return None
        removed = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed

    def is_empty(self):
        return self.head is None

    def display(self):
        current = self.head
        text = ""
        while current is not None:
            text += current.data + " -> "
            current = current.next
        return text + "NULL"

def run():
    name = "TEOPIZ"
    linked_list = LinkedList()

    print("\n--- Adding letters ---")
    for letter in name:
        linked_list.add(letter)
        print("Added", letter, "->", linked_list.display())

    print("\n--- Removing letters ---")
    while not linked_list.is_empty():
        removed = linked_list.remove()
        print("Removed", removed, "->", linked_list.display())

    print("\nThe linked list is now empty.")

if __name__ == "__main__":
    run()