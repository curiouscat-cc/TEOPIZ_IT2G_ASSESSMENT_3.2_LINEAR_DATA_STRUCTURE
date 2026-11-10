# Array program
# Assessment 3.2: Array Operations using TEOPIZ


def run():
    print("\n--- Running Array Program ---")
    default_name = "TEOPIZ"
    user_input = input(f"Enter your last name [Default: {default_name}]: ").strip().upper()
    name = user_input if user_input else default_name

    # Array with one slot per letter
    array = [None] * len(name)
    size = 0

    # Add each letter
    print("\n--- Adding letters ---")
    for letter in name:
        array[size] = letter
        size += 1
        print("Added", letter, "->", array)

    # Remove letters from the last index
    print("\n--- Removing letters ---")
    while size > 0:
        size -= 1
        removed = array[size]
        array[size] = None
        print("Removed", removed, "->", array)

    print("\nThe array is now empty.")


if __name__ == "__main__":
    run()