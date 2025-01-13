import datetime

def get_birthday_from_pesel(pesel: str) -> datetime.datetime:
    if len(pesel) != 11 or not pesel.isdigit():
        raise ValueError("PESEL musi składać się z 11 cyfr.")
    
    year = int(pesel[:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    
    # Określenie stulecia na podstawie miesięcy
    if 1 <= month <= 12:
        year += 1900
    elif 21 <= month <= 32:
        year += 2000
        month -= 20
    elif 41 <= month <= 52:
        year += 2100
        month -= 40
    elif 61 <= month <= 72:
        year += 2200
        month -= 60
    elif 81 <= month <= 92:
        year += 1800
        month -= 80
    else:
        raise ValueError("Nieprawidłowy miesiąc w PESEL.")

    return datetime.datetime(year, month, day)

def get_gender_from_pesel(pesel: str) -> str:
    if len(pesel) != 11 or not pesel.isdigit():
        raise ValueError("PESEL musi składać się z 11 cyfr.")
    
    gender_digit = int(pesel[9])
    return 'M' if gender_digit % 2 != 0 else 'F'

def validate_pesel(pesel: str) -> bool:
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
    checksum = (10 - (checksum % 10)) % 10
    
    return checksum == int(pesel[10])

# Przykład użycia
pesel = "44051401359"
print("Data urodzenia:", get_birthday_from_pesel(pesel))
print("Płeć:", get_gender_from_pesel(pesel))
print("Czy PESEL jest poprawny?:", validate_pesel(pesel))