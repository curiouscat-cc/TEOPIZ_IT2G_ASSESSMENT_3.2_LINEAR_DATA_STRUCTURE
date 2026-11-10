# Main program

import array_program
import linked_list_program
import stack_program
import queue_program


# Shows the menu options
def show_menu():
    print("\n==== LINEAR DATA STRUCTURES ====")
    print("1. Array")
    print("2. Linked List")
    print("3. Stack")
    print("4. Queue")
    print("5. Exit")


# Asks for a choice and runs the chosen program
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            array_program.run()
        elif choice == "2":
            linked_list_program.run()
        elif choice == "3":
            stack_program.run()
        elif choice == "4":
            queue_program.run()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()