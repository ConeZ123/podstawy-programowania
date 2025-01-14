## LAB 11 - Klasy

# Klasy BankAccount, Balance i Loan

Ten projekt składa się z trzech głównych klas: `BankAccount`, `Balance` oraz `Loan`, z których każda jest zaimplementowana w osobnym pliku.

## Klasa Balance
Klasa `Balance` reprezentuje stan konta.

### Konstruktor
Inicjalizuje wartość salda.

### Metody
- **`change(value)`**
  - Modyfikuje stan konta.
  - Wartość dodatnia: wpłata.
  - Wartość ujemna: wypłata (tylko jeśli nie prowadzi do salda ujemnego; w przeciwnym razie zwraca `false`).
- **`get()`**
  - Zwraca bieżące saldo.

## Klasa Loan
Klasa `Loan` reprezentuje pożyczkę z detalami dotyczącymi warunków spłaty.

### Konstruktor
Inicjalizuje pożyczkę z:
- Kwotą pożyczki.
- Stopą procentową.
- Okresem spłaty (w miesiącach).

Oblicza całkowitą kwotę do spłaty i przechowuje ją w obiekcie klasy `Balance`.

### Metody
- **`calculatePayment()`**
  - Zwraca wysokość miesięcznej raty.
- **`pay(value)`**
  - Zmniejsza saldo pożyczki o przekazaną kwotę spłaty.
- **`isPaidOff()`**
  - Zwraca `true`, jeśli pożyczka została w pełni spłacona; w przeciwnym razie `false`.

## Klasa BankAccount
Klasa `BankAccount` modeluje konto bankowe użytkownika z danymi osobowymi, saldem oraz zarządzaniem pożyczkami.

### Pola
- `firstName`: Imię użytkownika.
- `lastName`: Nazwisko użytkownika.
- `pesel`: Numer identyfikacyjny użytkownika (PESEL).
- `accountNumber`: Numer konta.
- Instancja klasy `Balance`.
- Lista obiektów klasy `Loan`.

### Metody
- **`deposit(amount)`**
  - Dodaje określoną kwotę do salda konta.
- **`withdraw(amount)`**
  - Odejmuje określoną kwotę z salda konta.
- **`createLoan(amount, term)`**
  - Tworzy nową pożyczkę o określonej wartości i okresie spłaty (w miesiącach).
- **`getLoans()`**
  - Zwraca listę wszystkich pożyczek powiązanych z kontem.
- **`payLoan(loanIndex)`**
  - Spłaca ratę pożyczki wskazanej przez jej indeks.
  - Kroki:
    1. Wywołaj `calculatePayment()` na wybranej pożyczce, aby uzyskać wysokość raty.
    2. Sprawdź, czy saldo konta jest wystarczające, korzystając z `get()` klasy `Balance`.
    3. Jeśli środki są wystarczające, wywołaj `pay()` na pożyczce z kwotą raty.

---
