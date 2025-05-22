def write_new_note():
    note = input("Enter your note:\n")
    with open("notes.txt", "w") as file:
        file.write(note + "\n")
    print("Note saved (overwritten).")


def view_notes():
    try:
        with open("notes.txt", "r") as file:
            print("\n--- Your Notes ---")
            print(file.read())
    except FileNotFoundError:
        print("No notes found. Write one first.")


def append_note():
    note = input("Enter your additional note:\n")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note appended.")


def main():
    while True:
        print("\nSimple Notepad")
        print("1. Write new note (overwrites)")
        print("2. View notes")
        print("3. Append to note")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            write_new_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            append_note()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-4.")

if __name__ == "__main__":
    main()
