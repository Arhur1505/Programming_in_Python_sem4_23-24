import datetime

def validate_pesel(pesel, birth_date, gender):
    '''Funkcja sprawdzająca poprawność numeru PESEL'''
    if not pesel.isdigit():
        raise ValueError("PESEL zawiera niedozwolone znaki")

    if len(pesel) != 11:
        raise ValueError("PESEL powinien składać się z 11 cyfr")

    birth_year = birth_date.year % 100
    if int(pesel[:2]) != birth_year:
        raise ValueError("Rok urodzenia w PESEL nie zgadza się z podaną datą")

    month_ = 0
    if 1800 <= birth_date.year <= 1899:
        month_ = 80
    elif 2000 <= birth_date.year <= 2099:
        month_ = 20
    elif 2100 <= birth_date.year <= 2199:
        month_ = 40
    elif 2200 <= birth_date.year <= 2299:
        month_ = 60

    birth_month = birth_date.month + month_

    if birth_month < 10:
        birth_month_str = f"0{birth_month}"
    else:
        birth_month_str = str(birth_month)

    if pesel[2:4] != birth_month_str:
        raise ValueError("Miesiąc urodzenia w PESEL nie zgadza się z podaną datą")

    if int(pesel[4:6]) != birth_date.day:
        raise ValueError("Dzień urodzenia w PESEL nie zgadza się z podaną datą")
    
    gender_digit = int(pesel[9])
    if gender == "kobieta" and gender_digit % 2 != 0:
        raise ValueError("Płeć w PESEL nie zgadza się z podaną płcią")
    elif gender == "mężczyzna" and gender_digit % 2 == 0:
        raise ValueError("Płeć w PESEL nie zgadza się z podaną płcią")

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    total = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - (total % 10)) % 10
    if control_digit != int(pesel[10]):
        raise ValueError("Niepoprawna suma kontrolna w PESEL")

    else:
        raise ValueError("Numer jest poprawny")