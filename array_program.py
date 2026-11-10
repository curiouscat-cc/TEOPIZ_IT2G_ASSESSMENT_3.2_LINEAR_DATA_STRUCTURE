
def run():
    name = "TEOPIZ"
    array = [None] * len(name)
    size = 0

    print("\n--- Adding letters ---")
    for letter in name:
        array[size] = letter
        size += 1
        print("Added", letter, "->", array)

    print("\n--- Removing letters ---")
    while size > 0:
        size -= 1
        removed = array[size]
        array[size] = None
        print("Removed", removed, "->", array)

    print("\nThe array is now empty.")

if __name__ == "__main__":
    run()