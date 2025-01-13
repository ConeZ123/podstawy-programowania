from students import *

def main():
    database = load_database()
    while True:
        print("\nMenu:")
        print("1. Dodaj nowego studenta")
        print("2. Edytuj dane studenta")
        print("3. Usuń studenta")
        print("4. Wyświetl studenta")
        print("5. Wyjście")
        choice = input("Wybierz działanie: ")
        if choice == "1":
            add_student(database)
        elif choice == "2":
            edit_student(database)
        elif choice == "3":
            delete_student(database)
        elif choice == "4":
            display_student(database)
        elif choice == "5":
            save_database(database)
            print("Baza danych została zapisana. Do widzenia!")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()