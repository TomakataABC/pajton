import random as rnd

veta_1 = 'Zkus a uvidíš: '
veta_2 = 'Zkus platné číslo... díky'


def run():
    y = rnd.randint(1, 50)
    ask(y)


def ask(y):
    try:
        x = int(input(veta_1))
    except:
        print(veta_2)
        ask(y)

    check(x, y)


def check(x, y):
    if x == y:
        print('----------------------------------------------------------------')
        print('Gratuluji, vyhrál/a jsi!')
        print('----------------------------------------------------------------')
    else:
        if x > y:
            print('Číslo je menší než Váš odhad.')
        else:
            print('Číslo je větší než Váš odhad.')
        ask(y)


run()
