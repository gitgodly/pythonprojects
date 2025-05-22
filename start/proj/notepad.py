import json
import os
from classnote import Note  #  import the class

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            raw = json.load(file)
            return [Note.from_dict(n) for n in raw]
    return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump([n.to_dict() for n in notes], file, indent=2)

def add_note():
    title = input("Title: ")
    content = input("Content:\n")
    note = Note(title, content)
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Note added.")

def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes yet.")
        return
    for note in notes:
        print(f"\n[{note.timestamp}] {note.title}\n{note.content}")
        print("-" * 30)

def main():
    while True:
        print("\n📘 Notepad Menu")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
