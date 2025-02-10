import card
import pesel
import average
import logging
import datetime

logging.basicConfig(filename="1.log", filemode='w', format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('Zadanie 1')

try:
    card.card_Luhn('924803')
except ValueError as err:
    logger.info(err)

try:
    card.card_Luhn('1234567898765437')
except ValueError as err:
    logger.info(err)

try:
    card.card_Luhn('91234567891234564')
except ValueError as err:
    logger.info(err)

try:
    card.card_Luhn('1234567891234563')
except ValueError as err:
    logger.info(err)

logger.info('Zadanie 2')

try:
    pesel.validate_pesel('02070803628', datetime.date(1902,7,8), 'kobieta')
except ValueError as err:
    logger.info(err)
try:
    pesel.validate_pesel('02270803624', datetime.date(2002,7,8), 'kobieta')
except ValueError as err:
    logger.info(err)
try:
    pesel.validate_pesel('02270812350', datetime.date(2002,7,8), 'mężczyzna')
except ValueError as err:
    logger.info(err)

logger.info('Zadanie 3')

try:
    average_age = average.calculate_average_age('daty.in', strict_mode=True)
    print(f"Średni wiek osób z pliku: {average_age:.2f} lat")
except ValueError as err:
    logger.info(err)

try:
    average_age = average.calculate_average_age('daty.in', strict_mode=False)
    print(f"Średni wiek osób z pliku: {average_age:.2f} lat")
except ValueError as err:
    logger.info(err)