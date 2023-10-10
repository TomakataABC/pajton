import os
import sys
import time

from colorama import Fore, Style, Back

header = f"{Fore.GREEN}======--- {Fore.BLUE}{Style.BRIGHT}{Back.LIGHTRED_EX} Ballin Program {Style.RESET_ALL}{Fore.GREEN} ---======"
footer = f"{Fore.GREEN}------------------------------------{Style.RESET_ALL}"
inputAsk = f"{Fore.BLUE}Vaše volba? {Style.RESET_ALL}"
invalidOption = f"{Back.LIGHTRED_EX}{Fore.BLACK} Neplatná volba {Style.RESET_ALL}"


def clear():
    os.system('cls')
    print('\n\n\n\n\n\n\n\n\n\n\n ')


def mainMenu():
    clear()
    print(header)
    print('')
    print(f'        {Fore.LIGHTBLUE_EX}{Style.DIM}[1]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}BF Data fetcher')
    print(f'            {Fore.LIGHTBLUE_EX}{Style.DIM}[2]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}BALLS?')
    print(f'             {Fore.LIGHTBLUE_EX}{Style.DIM}[3]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Exit')
    print(footer)

    choice = int(input(inputAsk))

    menuOptions = {
        1: bfMenu,
        2: bfMenu,
        3: exitProcess,
    }

    try:
        if choice in menuOptions:
            menuOptions[choice]()
        else:
            invalidChoice(mainMenu)
    except ValueError:
        invalidChoice(mainMenu)


def bfMenu():
    clear()
    print(header)
    print('')
    print(f'{Fore.MAGENTA}      ⮑ BF Data fetcher 3000 ⮐')
    print('')
    print(f'            {Fore.LIGHTBLUE_EX}{Style.DIM}[1]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Databáze')
    print(f'             {Fore.LIGHTBLUE_EX}{Style.DIM}[2]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Služby')
    print(f'              {Fore.LIGHTBLUE_EX}{Style.DIM}[3]{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}Zpět')
    print(footer)

    choice = int(input(inputAsk))

    menuOptions = {
        1: bfMenu,
        2: bfMenu,
        3: mainMenu,
    }

    try:
        if choice in menuOptions:
            menuOptions[choice]()
        else:
            invalidChoice(bfMenu)
    except ValueError:
        invalidChoice(bfMenu)


def invalidChoice(menu):
    clear()
    print(invalidOption)
    time.sleep(2)
    menu()


def exitProcess():
    clear()
    print(f"{Back.RED}{Fore.BLACK} Na viděnou :) {Back.RESET}{Fore.RESET}")
    sys.exit(0)


mainMenu()
