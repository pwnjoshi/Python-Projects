# Note Taking App

FILE_NAME= "myNotes.txt"

def show_menu():
  print("\n--- Note Taking App Menu ---")
  print("1. Add a new note")
  print("2. View all notes")
  print("3. Delete all notes")
  print("4. Exit")
1
def add_note():
  note = input("Enter your note: ")
  with open(FILE_NAME, "a") as file:
    file.write(note + "\n")
  print("Note added successfully!")

def view_notes():
  try:
    with open(FILE_NAME, "r") as file:
      content = file.read()
      if content:
        print("\n--- Your Notes ---")
        print(content)
      else:
        print("No notes found.")
  except FileNotFoundError:
    print("No notes found.")

def delete_notes():
  confirm=input("Are you sure you want to delete all notes? (Yes/No): ")
  if confirm.lower() == "yes":
    with open(FILE_NAME, "w") as file:
      pass
    print("All notes deleted successfully!")
  else:
    print("Note deletion canceled.")
while True:
  show_menu()
  choice = input("Enter your choice (1/2/3): ")

  if choice == "1":
    add_note()
  elif choice == "2":
    view_notes()
  elif choice == "3":
    delete_notes()
  elif choice == "4":
    print("Exiting Note Taking app. Good Bye! ")
    break
  else:
    print("Invalid choice. Please enter 1, 2, or 3.")
