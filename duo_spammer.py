import random
import sys

from PyRandomNameGenerator import generateRandomName
import requests

# Potřeba souboru http.txt ve stejné složce jako python soubor

proxies = set()
agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
}

inp = input('Email ')
count = int(input('# of emails '))

epr = '@' + inp.split('@')[1].strip()

print('The email was modified: ' + inp.replace(epr, '+' + random.randint(0, 10).__str__() + epr))

verify = input('Continue? y/N ')

if verify != 'y':
    sys.exit('Okay, stopping...')


def loadProxies():
    with open('./http.txt', 'r') as file:
        i = 0
        fline = file.readlines()
        x = len(fline)
        for line in fline:
            proxies.add(line.strip())
            loadbar(i + 1, x, prefix='Loading proxies', length=50)
            i = i + 1


def startSpam():
    
    print('Starting spam')

    for x in range(count):
        proxy = {'http': random.choice(list(proxies))}
        mail = inp.replace(epr, '+' + x.__str__() + epr)

        payload = {
            'signal': '',
            'timezone': 'UTC',
            'fromLanguage': 'en',
            'age': random.randint(15, 89),
            'email': mail,
            'identifier': '',
            'name': '',
            'password': random.random().__str__(),
            'username': generateRandomName().replace(' ', random.randint(10, 99).__str__()),
            'landingUrl': 'https://www.duolingo.com/',
            'initialReferrer': '$direct',
            'lastReferrer': ''
        }

        re = requests.post('', #URL adresa odebrána z očividných důvodů
                           json=payload,
                           headers=agent,
                           proxies=proxy)

        print(re.text)


def loadbar(iteration, total, prefix='', length=100, fill='|'):
    ('{0:.' + str(1) + 'f}').format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '/' * (length - filled_length)
    print(f'\r{prefix} {bar}', end='\r')
    if iteration == total:
        print()


loadProxies()
startSpam()
