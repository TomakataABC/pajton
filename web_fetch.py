import os
import sys
import time

from colorama import Fore, Style, Back

header = f"{Fore.GREEN}======--- {Fore.BLUE}{Style.BRIGHT}{Back.LIGHTRED_EX} Ballin Program {Fore.GREEN}{Back.RESET} ---======"
footer = f"{Fore.GREEN}------------------------------------"
inputAsk = f"{Fore.BLUE}Vaše volba? {Fore.RESET}"
invalidOption = f"{Back.RED}{Fore.BLACK} Neplatná volba {Back.RESET}{Fore.RESET}"


def clear():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

def mainMenu():
    clear()
    print(header)
    print(f'        {Fore.BLUE}{Style.DIM}[{Style.BRIGHT}1{Style.DIM}] {Fore.LIGHTGREEN_EX}BF Data fetcher')
    print(f'            {Fore.BLUE}{Style.DIM}[{Style.BRIGHT}2{Style.DIM}] {Fore.LIGHTGREEN_EX}BALLS?')
    print(f'             {Fore.BLUE}{Style.DIM}[{Style.BRIGHT}3{Style.DIM}] {Fore.LIGHTGREEN_EX}Exit')
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
    print(f'            {Fore.BLUE}{Style.DIM}[{Style.BRIGHT}1{Style.DIM}] {Fore.LIGHTGREEN_EX}Databáze')
    print(f'             {Fore.BLUE}{Style.DIM}[{Style.BRIGHT}2{Style.DIM}] {Fore.LIGHTGREEN_EX}Služby')
    print(f'              {Fore.BLUE}{Style.DIM}[{Style.BRIGHT}3{Style.DIM}] {Fore.LIGHTGREEN_EX}Zpět')
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
