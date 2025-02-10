def card_Luhn(number):
    '''Funkcja sprawdzająca poprawność numeru karty kredytowej'''
    try:
        number = list(map(int, number))
    except ValueError:
        print('Zły numer')
        raise
    if len(number) != 16:
        raise ValueError('Numer za krótki')

    sum_ = 0
    for i, j in enumerate(number):
        if i % 2 == 0:
            j *= 2
            if j >= 10:
                j = sum(map(int, str(j)))
        sum_ += j

    if sum_ % 10 != 0:
        raise ValueError('Błędny numer')
    else:
        raise ValueError('Numer jest poprawny')