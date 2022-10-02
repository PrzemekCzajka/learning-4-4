#Kalkulator

import def_func
import logging
from enum import IntEnum
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

menu_dzialania = IntEnum("Menu_dzialania", "Dodawanie Odejmowanie Mnożenie Dzielenie")

wybor = int(input("""Wybierz ktore działanie chcesz wykonać wpisując liczbę: 
1. Dodawanie
2. Odejmowanie
3. Mnożenie
4. Dzielenie
"""))



if wybor == menu_dzialania.Dodawanie:
    try:
        a = int(input("Podaj pierwszą liczbę: "))
    except ValueError:
        print("Miała być liczba!")
    try:
        b = int(input("Podaj drugą liczbę: "))
    except ValueError:
        print("Miała być liczba!")
    c = a + b
    logging.info("Dodajemy %s do %s" % (a, b))
    print("Wynik dodawania to: ", (c))
elif wybor == menu_dzialania.Odejmowanie:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    c = a - b
    logging.info("Odejmujemy %s od %s" % (a, b))
    print("Wynik odejmowania to: ",(c))
elif wybor == menu_dzialania.Mnożenie:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    logging.info("Mnożymy %s przez %s" % (a, b))
    print("Wynik mnożenia to: ", (a*b))
elif wybor == menu_dzialania.Dzielenie:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    def_func.dzielenie(a, b)
    logging.info("Dzielimy %s przez %s" % (a, b))
else:
    print("Niewłaściwy wybór!")
    exit(1)
