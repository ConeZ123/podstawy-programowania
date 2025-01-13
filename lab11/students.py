import json
import os

def load_database(filename="students.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}

def save_database(database, filename="students.json"):
    with open(filename, "w") as file:
        json.dump(database, file, indent=4)

def add_student(database):
    index = input("Podaj numer indeksu: ")
    if index in database:
        print("Student o takim numerze indeksu już istnieje!")
        return
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    birth_date = input("Podaj datę urodzenia (YYYY-MM-DD): ")
    gender = input("Podaj płeć (M/F): ")
    database[index] = {
        "name": name,
        "surname": surname,
        "birth_date": birth_date,
        "gender": gender
    }
    print("Dodano nowego studenta.")

def edit_student(database):
    index = input("Podaj numer indeksu studenta do edycji: ")
    if index not in database:
        print("Nie znaleziono studenta o takim numerze indeksu.")
        return
    print("Pozostaw pole puste, jeśli nie chcesz zmieniać wartości.")
    name = input(f"Imię ({database[index]['name']}): ") or database[index]['name']
    surname = input(f"Nazwisko ({database[index]['surname']}): ") or database[index]['surname']
    birth_date = input(f"Data urodzenia ({database[index]['birth_date']}): ") or database[index]['birth_date']
    gender = input(f"Płeć ({database[index]['gender']}): ") or database[index]['gender']
    database[index] = {
        "name": name,
        "surname": surname,
        "birth_date": birth_date,
        "gender": gender
    }
    print("Zaktualizowano dane studenta.")

def delete_student(database):
    index = input("Podaj numer indeksu studenta do usunięcia: ")
    if index in database:
        del database[index]
        print("Usunięto studenta.")
    else:
        print("Nie znaleziono studenta o takim numerze indeksu.")

def display_student(database):
    index = input("Podaj numer indeksu studenta: ")
    if index in database:
        student = database[index]
        print(f"Imię: {student['name']}")
        print(f"Nazwisko: {student['surname']}")
        print(f"Data urodzenia: {student['birth_date']}")
        print(f"Płeć: {student['gender']}")
    else:
        print("Nie znaleziono studenta o takim numerze indeksu.")

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