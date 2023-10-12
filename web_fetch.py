import os
import sys
import time
import requests

from tqdm import tqdm
from bs4 import BeautifulSoup
from colorama import Fore, Style, Back

header = f"{Fore.GREEN}======--- {Fore.BLUE}{Style.BRIGHT}{Back.LIGHTRED_EX} Ballin Program {Style.RESET_ALL}{Fore.GREEN} ---======"
footer = f"{Fore.GREEN}------------------------------------{Style.RESET_ALL}"
inputAsk = f"{Fore.BLUE}Vaše volba? {Style.RESET_ALL}"

webAgent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}


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
            printError(mainMenu, 'Neplatná volba!')
    except ValueError:
        printError(mainMenu, 'Neplatná volba!')


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
        1: fetchBfData,
        2: fetchBfData,
        3: mainMenu,
    }

    fetchLink = {
        1: 'https://breachforums.is/Forum-Databases',
        2: 'https://breachforums.is/Forum-Services',
        3: '4',
    }

    try:
        if choice in menuOptions:
            menuOptions[choice](fetchLink[choice])
        else:
            printError(bfMenu, 'Neplatná volba!')
    except ValueError:
        printError(bfMenu, 'Neplatná volba!')


def fetchBfData(link):
    clear()

    print('Hledání informací...')
    req_reply = requests.get(link,
                             headers=webAgent)

    if req_reply.status_code != 200:
        printError(bfMenu, f'Nepodařilo se získat data! ({req_reply.status_code})')
    else:
        processData(req_reply)


def processData(data):
    print('Třídění dat...')
    bs = BeautifulSoup(data.content, 'html.parser')
    table = bs.find('table', class_='tborder clear')
    rows = table.find_all('tr', class_='inline_row')

    del rows[0]
    del rows[0]

    sorted_data = []

    for i in tqdm(range(len(rows)), desc='Pogres'):
        span = rows[i].find('span', class_='subject_new')

        name = span.find('a').text
        link = f'https://breachforums.is/{span.find("a")["href"]}'

        sorted_data.append([name, link])

    print('Hotovo!')
    time.sleep(1.5)
    presentBfData(sorted_data)


def presentBfData(data):
    clear()
    for i in range(len(data)):
        print(f'[{i+1}]')
        print(f'{Fore.LIGHTBLUE_EX}{data[i][0]}')
        print(f'{Fore.BLUE}{data[i][1]}{Fore.RESET}')
        print('')

    input('Zmáčkni enter pro pokračování...')
    mainMenu()


def printError(menu, text):
    clear()
    print(errorText(text))
    time.sleep(2)
    menu()
    return 


def errorText(text):
    return f"{Back.LIGHTRED_EX}{Fore.BLACK} {text} {Style.RESET_ALL}"


def exitProcess():
    clear()
    print(f"{Back.RED}{Fore.BLACK} Na viděnou :) {Back.RESET}{Fore.RESET}")
    sys.exit(0)


mainMenu()
