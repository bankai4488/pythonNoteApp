   # Note Taking App

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note added successfully")


def view_notes():
    with open("notes.txt", "r") as f:
        notes = f.read()
        print("\n--- All Notes ---")
        print(notes)


def clear_notes():
    with open("notes.txt", "w") as f:
        pass
    print("All notes cleared")


def main():
    while True:
        print("\n1) Add a note")
        print("2) View all notes")
        print("3) Clear all notes")
        print("4) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            clear_notes()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
main()

##developed by Pranish