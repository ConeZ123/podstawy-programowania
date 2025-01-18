import json
import os

DB_FILE = "students.json"

def load_database():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def save_database(database):
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(database, file,)

def add_student(database):
    index = input("Podaj numer indeksu studenta: ")
    if index in database:
        print("Student o tym numerze indeksu już istnieje.")
        return

    name = input("Podaj imię i nazwisko studenta: ")
    birth_date = input("Podaj datę urodzenia studenta (YYYY-MM-DD): ")
    gender = input("Podaj płeć studenta (M/F): ")

    database[index] = {
        "name": name,
        "birth_date": birth_date,
        "gender": gender
    }
    print("Student został dodany.")

def edit_student(database):
    index = input("Podaj numer indeksu studenta do edycji: ")
    if index not in database:
        print("Nie znaleziono studenta o podanym numerze indeksu.")
        return

    print(f"Obecne dane: {database[index]}")
    name = input("Podaj nowe imię i nazwisko studenta (pozostaw puste, aby nie zmieniać): ")
    birth_date = input("Podaj nową datę urodzenia studenta (YYYY-MM-DD, pozostaw puste, aby nie zmieniać): ")
    gender = input("Podaj nową płeć studenta (M/F, pozostaw puste, aby nie zmieniać): ")

    if name:
        database[index]["name"] = name
    if birth_date:
        database[index]["birth_date"] = birth_date
    if gender:
        database[index]["gender"] = gender

    print("Dane studenta zostały zaktualizowane.")

def delete_student(database):
    index = input("Podaj numer indeksu studenta do usunięcia: ")
    if index in database:
        del database[index]
        print("Student został usunięty.")
    else:
        print("Nie znaleziono studenta o podanym numerze indeksu.")

def display_student(database):
    index = input("Podaj numer indeksu studenta do wyświetlenia: ")
    if index in database:
        student = database[index]
        print(f"Numer indeksu: {index}")
        print(f"Imię i nazwisko: {student['name']}")
        print(f"Data urodzenia: {student['birth_date']}")
        print(f"Płeć: {student['gender']}")
    else:
        print("Nie znaleziono studenta o podanym numerze indeksu.")

def main():
    database = load_database()

    while True:
        print("\nWybierz działanie:")
        print("1. Dodaj nowego studenta")
        print("2. Edytuj dane studenta")
        print("3. Usuń studenta")
        print("4. Wyświetl studenta")
        print("5. Wyjście")

        choice = input("Twój wybór: ")

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
