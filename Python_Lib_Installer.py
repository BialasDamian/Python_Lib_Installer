from os import system
from ladowanie import Smtplib,Pylance,Python,numPy,wget,Seaborn,Matplotlib
from wykrywanie_obiektu import WykrywanieTwarzy

import msvcrt
import time
import sys
import msvcrt
from time import sleep

def menu1():
    while True:
        try:
            wybor = int(input("""Witam w programie instalacyjnym\n===========MENU============\nCo chciałbyś zainstalować?\n
        1.Oprogramowanie Python\n
        2.Oprogramowanie Pylance\n
        3.Biblioteki do języka Python\n
        4.Zakończ program\n
        Wybierz opcję 1, 2, 3 lub 4 \n"""))
            
            if wybor == 1:
                decyzjapython = input("\nCzy chcesz zainstalować środowisko Python ? (t/n) \n")
                if decyzjapython == 't':
                    system('cls')
                    Python()
                    wyborpython1 = (input("""Co chcesz teraz zrobić?\n
                            1.Cofnij do głównego menu\n
                            2.Zakończ program\n"""))
                    while True:
                        try:
                            if wyborpython1 == '1':
                                system('cls')
                                menu1()
                            elif wyborpython1 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                elif decyzjapython == 'n':
                    system('cls')
                    wyborpython2 = (input("""Co chcesz teraz zrobić?\n
                            1.Cofnij do głównego menu\n
                            2.Zakończ program\n"""))
                    while True:
                        try:
                            if wyborpython2 == '1':
                                system('cls')
                                menu1()
                            elif wyborpython2 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
            elif wybor == 2:
                system('cls')
                decyzjapylance = input("\nCzy chcesz zainstalować środowisko Python ? (t/n) \n")
                if decyzjapylance == 't':
                    system('cls')
                    Pylance()
                    wyborpylance1 = (input("""Co chcesz teraz zrobić?\n
                            1.Cofnij do głównego menu\n
                            2.Zakończ program\n"""))
                    while True:
                        try:
                            if wyborpylance1 == '1':
                                system('cls')
                                menu1()
                            elif wyborpylance1 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                elif decyzjapylance == 'n':
                    system('cls')
                    wyborpylance2 = (input("""Co chcesz teraz zrobić?\n
                            1.Cofnij do głównego menu\n
                            2.Zakończ program\n"""))
                    while True:
                        try:
                            if wyborpylance2 == '1':
                                system('cls')
                                menu1()
                            elif wyborpylance2 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
            elif wybor == 3:
                system('cls')
                biblioteka = input("""Jaką bibliotekę chcesz zainstalować?\n
                1.    Biblioteka Smtplib\n
                2.    Biblioteka Matplotlib\n
                3.    Biblioteka wget\n
                4.    Biblioteka Seaborn\n
                5.    Cofnij do menu\n
                6.    Zamknij program\n""")
                while True:
                    try:
                        if  biblioteka == '1':
                            system('cls')
                            decyzja1 = (input('Czy na pewno chcesz zainstalować bibliotekę Smtplib (t/n) ?'))
                            if decyzja1 == 't':
                                system('cls')
                                Smtplib()
                                wybor31 = input("""Co chcesz teraz zrobić?\n
                                1.Cofnij do poprzedniego menu\n
                                2.Zakończ program\n""")
                                while True:
                                    try:
                                        if wybor31 == '1':
                                            system('cls')
                                            biblioteka1()
                                        elif wybor31 == '2':
                                            system('cls')
                                            print("Naciśnij dowolny klawisz by zakończyć program\n")
                                            msvcrt.getch()
                                            sys.exit(0)
                                    except ValueError:
                                        system('cls')
                                        print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                            elif decyzja1 == 'n':
                                system('cls')
                                wybor32 = input("""Co chcesz teraz zrobić?\n
                                1.Cofnij do poprzedniego menu\n
                                2.Zakończ program\n""")
                                while True:
                                    try:
                                        if wybor32 == '1':
                                            system('cls')
                                            biblioteka1()
                                        elif wybor32 == '2':
                                            system('cls')
                                            print("Naciśnij dowolny klawisz by zakończyć program\n")
                                            msvcrt.getch()
                                            sys.exit(0)
                                    except ValueError:
                                        system('cls')
                                        print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                        elif biblioteka == '2':
                            system('cls')
                            decyzja2 = (input('Czy na pewno chcesz zainstalować bibliotekę Matplotlib  (t/n) ?'))
                            if decyzja2 == 't':
                                system('cls')
                                Matplotlib()
                                wybor33 = input("""Co chcesz teraz zrobić?\n
                                1.Cofnij do poprzedniego menu\n
                                2.Zakończ program\n""")
                                while True:
                                    try:
                                        if wybor33 == '1':
                                            system('cls')
                                            biblioteka1()
                                        elif wybor33 == '2':
                                            system('cls')
                                            print("Naciśnij dowolny klawisz by zakończyć program\n")
                                            msvcrt.getch()
                                            sys.exit(0)
                                    except ValueError:
                                        system('cls')
                                        print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                            elif decyzja2 == 'n':
                                system('cls')
                                wybor34 = input("""Co chcesz teraz zrobić?\n
                                1.Cofnij do poprzedniego menu\n
                                2.Zakończ program\n""")
                                while True:
                                    try:
                                        if wybor34 == '1':
                                            system('cls')
                                            biblioteka1()
                                        elif wybor34 == '2':
                                            system('cls')
                                            print("Naciśnij dowolny klawisz by zakończyć program\n")
                                            msvcrt.getch()
                                            sys.exit(0)
                                    except ValueError:
                                        system('cls')
                                        print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                        elif  biblioteka == '3':
                            system('cls')
                            decyzja3 = (input('Czy na pewno chcesz zainstalować bibliotekę wget  (t/n) ?'))
                            if decyzja3 == 't':
                                system('cls')
                                wget()
                                wybor35 = input("""Co chcesz teraz zrobić?\n
                                1.Cofnij do poprzedniego menu\n
                                2.Zakończ program\n""")
                                while True:
                                    try:
                                        if wybor35 == '1':
                                            system('cls')
                                            biblioteka1()
                                        elif wybor35 == '2':
                                            system('cls')
                                            print("Naciśnij dowolny klawisz by zakończyć program\n")
                                            msvcrt.getch()
                                            sys.exit(0)
                                    except ValueError:
                                        system('cls')
                                        print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                            elif decyzja3 == 'n':
                                system('cls')
                                wybor30 = input("""Co chcesz teraz zrobić?\n
                                1.Cofnij do poprzedniego menu\n
                                2.Zakończ program\n""")
                                while True:
                                    try:
                                        if wybor30 == '1':
                                            system('cls')
                                            biblioteka1()
                                        elif wybor30 == '2':
                                            system('cls')
                                            print("Naciśnij dowolny klawisz by zakończyć program\n")
                                            msvcrt.getch()
                                            sys.exit(0)
                                    except ValueError:
                                        system('cls')
                                        print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                        elif biblioteka == '4':
                            system('cls')
                            decyzja4 = (input('Czy na pewno chcesz zainstalować bibliotekę Seaborn  (t/n) ?'))
                            if decyzja4 == 't':
                                system('cls')
                                Seaborn()
                                wybor37 = input("""Co chcesz teraz zrobić?\n
                                1.Cofnij do poprzedniego menu\n
                                2.Zakończ program\n""")
                                while True:
                                    try:
                                        if wybor37 == '1':
                                            system('cls')
                                            biblioteka1()
                                        elif wybor37 == '2':
                                            system('cls')
                                            print("Naciśnij dowolny klawisz by zakończyć program\n")
                                            msvcrt.getch()
                                            sys.exit(0)
                                    except ValueError:
                                        system('cls')
                                        print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                            elif decyzja4 == 'n':
                                system('cls')
                                wybor38 = input("""Co chcesz teraz zrobić?\n
                                1.Cofnij do poprzedniego menu\n
                                2.Zakończ program\n""")
                                while True:
                                    try:
                                        if wybor38 == '1':
                                            system('cls')
                                            biblioteka1()
                                        elif wybor38 == '2':
                                            system('cls')
                                            print("Naciśnij dowolny klawisz by zakończyć program\n")
                                            msvcrt.getch()
                                            sys.exit(0)
                                    except ValueError:
                                        system('cls')
                                        print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                        elif biblioteka == '5':
                            system('cls')
                            menu1()
                        elif biblioteka == '6':
                            system('cls')
                            print("Naciśnij dowolny klawisz by zakończyć program\n")
                            msvcrt.getch()
                            sys.exit(0)
                    except ValueError:
                        system('cls')
                        print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1, 2, 3, 4, 5 lub 6") 
            
            
            elif wybor == 4:
                print("Naciśnij dowolny klawisz by zakończyć program\n")
                msvcrt.getch()
                sys.exit(0)
        except ValueError:
            system('cls')
            print("\nWprowadzono nieprawidłową wartość. Wprowadź wartość 1, 2, 3 lub 4 !\nKliknij Enter by kontynuować")
            msvcrt.getch()
            
       






def biblioteka1():
    biblioteka = input("""Jaką bibliotekę chcesz zainstalować?\n
        1.    Biblioteka Smtplib\n
        2.    Biblioteka Matplotlib\n
        3.    Biblioteka wget\n
        4.    Biblioteka Seaborn\n
        5.    Cofnij do menu\n
        6.    Zamknij program\n""")
    
    while True:
        try:
            if  biblioteka == '1':
                system('cls')
                decyzja1 = (input('Czy na pewno chcesz zainstalować bibliotekę Smtplib (t/n)?'))
                if decyzja1 == 't':
                    system('cls')
                    Smtplib()
                    wybor31 = input("""Co chcesz teraz zrobić?\n
                    1.Cofnij do poprzedniego menu\n
                    2.Zakończ program\n""")
                    while True:
                        try:
                            if wybor31 == '1':
                                system('cls')
                                biblioteka()
                            elif wybor31 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                elif decyzja1 == 'n':
                    system('cls')
                    wybor32 = input("""Co chcesz teraz zrobić?\n
                    1.Cofnij do poprzedniego menu\n
                    2.Zakończ program\n""")
                    while True:
                        try:
                            if wybor32 == '1':
                                system('cls')
                                biblioteka()
                            elif wybor32 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
            elif biblioteka == '2':
                system('cls')
                decyzja2 = (input('Czy na pewno chcesz zainstalować bibliotekę Matplotlib  (t/n) ?'))
                if decyzja2 == 't':
                    system('cls')
                    Matplotlib()
                    wybor33 = input("""Co chcesz teraz zrobić?\n
                    1.Cofnij do poprzedniego menu\n
                    2.Zakończ program\n""")
                    while True:
                        try:
                            if wybor33 == '1':
                                system('cls')
                                biblioteka()
                            elif wybor33 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                elif decyzja2 == 'n':
                    system('cls')
                    wybor34 = input("""Co chcesz teraz zrobić?\n
                    1.Cofnij do poprzedniego menu\n
                    2.Zakończ program\n""")
                    while True:
                        try:
                            if wybor34 == '1':
                                system('cls')
                                biblioteka()
                            elif wybor34 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
            elif  biblioteka == '3':
                system('cls')
                decyzja3 = (input('Czy na pewno chcesz zainstalować bibliotekę wget  (t/n) ?'))
                if decyzja3 == 't':
                    system('cls')
                    wget()
                    wybor35 = input("""Co chcesz teraz zrobić?\n
                    1.Cofnij do poprzedniego menu\n
                    2.Zakończ program\n""")
                    while True:
                        try:
                            if wybor35 == '1':
                                system('cls')
                                biblioteka()
                            elif wybor35 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                elif decyzja3 == 'n':
                    system('cls')
                    wybor36 = input("""Co chcesz teraz zrobić?\n
                    1.Cofnij do poprzedniego menu\n
                    2.Zakończ program\n""")
                    while True:
                        try:
                            if wybor36 == '1':
                                system('cls')
                                biblioteka()
                            elif wybor36 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
            elif biblioteka == '4':
                system('cls')
                decyzja4 = (input('Czy na pewno chcesz zainstalować bibliotekę Seaborn  (t/n) ?'))
                if decyzja4 == 't':
                    system('cls')
                    Seaborn()
                    wybor37 = input("""Co chcesz teraz zrobić?\n
                    1.Cofnij do poprzedniego menu\n
                    2.Zakończ program\n""")
                    while True:
                        try:
                            if wybor37 == '1':
                                system('cls')
                                biblioteka()
                            elif wybor37 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
                elif decyzja4 == 'n':
                    system('cls')
                    wybor38 = input("""Co chcesz teraz zrobić?\n
                    1.Cofnij do poprzedniego menu\n
                    2.Zakończ program\n""")
                    while True:
                        try:
                            if wybor38 == '1':
                                system('cls')
                                biblioteka()
                            elif wybor38 == '2':
                                system('cls')
                                print("Naciśnij dowolny klawisz by zakończyć program\n")
                                msvcrt.getch()
                                sys.exit(0)
                        except ValueError:
                            system('cls')
                            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1 lub 2.")
            elif biblioteka == '5':
                system('cls')
                menu1()
            elif biblioteka == '6':
                system('cls')
                print("Naciśnij dowolny klawisz by zakończyć program\n")
                msvcrt.getch()
                sys.exit(0)
        except ValueError:
            system('cls')
            print("\nWprowadzona wartość jest nieprawidłowa, wprowadź wartość 1, 2, 3, 4, 5 lub 6") 
menu1()