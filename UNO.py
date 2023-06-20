import random
import time
import sys

welcome = '   Welcome to UNO   '
print(welcome.center(len(welcome)+109,'$'))
players = []
stack_cards = []
t = 500
ig = 6


def uy(a, z):
    while z <= ig:
        name = input(f"\nPlayer№{a}. What is your name?: ")
        if name in players:
            print("This nickname is used. Please enter another nickname!")
            continue

        if len(name) > 0:
            message = f"Hello {name}. Let's play UNO. Are you ready? "
            print(message)
            a += 1
            z += 1
            players.append(name)
        elif len(name) <= 0:
            name2 = "Please. Enter your name one more times"
            print(name2)


uy(1, 1)


def pl():
    print("\nOur players are: " + ', '.join(players))
    for index in range(2, 0, -1):
        time.sleep(1)
    print(f"\nThe game goes up to {t} points")
    for index in range(2, 0, -1):
        time.sleep(1)
    for t_timer in range(3, -1, -1):
        sys.stdout.write("\r")
        sys.stdout.write("The game will start in : {:2d}".format(t_timer))
        sys.stdout.flush()
        time.sleep(1.2)

    sys.stdout.write("\rShuffle and deal the cards")
    for index in range(2, 0, -1):
        time.sleep(1.2)
        random.shuffle(stack_cards)
    print("\nCounting the points\n")
    for index in range(2, 0, -1):
        time.sleep(1.2)


pl()
# Наборы карт в Uno

cards1 = 16 * [1, 2, 3, 4, 5, 6, 7, 8, 9]  # *16
cards2 = 8 * [0, 0, 0, 0]  # *8
cards3 = {'+2': '20', 'SKIP': '20', 'REVERSE': '20'}  # *16
cards4 = {'+4': '50', 'COLOUR': '50'}  # *8
cards5 = cards3 | cards4

for i in cards1:
    stack_cards.append(i)
for i in cards2:
    stack_cards.append(i)
for i in cards3:
    stack_cards.append(i)
for i in cards4:
    stack_cards.append(i)
# Остаток карт 1 игрока


result = []
d = 1

ee = {}
u = 0
result2 = []
result1 = []
btl = False
while True:
    if any(u >= t for u in result2):
        print("\nWin " + str(min(ee, key=ee.get)) + " with " + str(min(ee.values())) + " points.\nOur "
                                                                                       "congratulations!!!\n")
        while True:
            play_again = input("\nPlay again? (Yes/No): ")
            if play_again.lower() == "yes":
                result2 = [i * 0 for i in result2]
                del result1[0:3]
                del players[:]
                d = 1
                uy(1, 1)
                pl()
                break
            elif play_again.lower() == "no":
                print("Good Bye;) See you later!")
                btl = True
                break
            else:
                print("Please enter: Yes or No\n")
                time.sleep(2)
        if btl:
            break

    list1 = ig * [0]
    result1 = result2.copy()
    result = []
    for el in list1:
        if el == 0:
            result1.append(el)
            el += 1
        else:
            break

    gh = random.randint(0, (ig - 1))

    for s in range(len(players)):
        if s == gh:
            print(f"\n" + players[s].upper() + " = Win")
            print("Player " + players[s].upper() + f" = 0 points")
            p2 = 0
            result.append(p2)

        else:
            l = random.randint(0, 32)  # рандомит k
            m = (random.sample(stack_cards, k=l))  # рандомит кол-во остатка карт
            all_players_cards = ','.join(str(j) for j in m)  # записывает карты в строку
            print(f"\n" + players[s].upper() + f" = {all_players_cards}")
            ll = [cards5.get(i, i) for i in m]  # присваивает эквивалент картам из словаря
            p1 = int(sum([int(item) for item in ll]))
            gg = ("Player " + players[s].upper() + f" = {p1} points")
            print(gg)
            result.append(p1)


    def is_prime(result):
        global result2
        result2 = [x + y for x, y in zip(result, result1)]
        for b in range(1, 5, 1):
            if b <= 2:
                return result2
            else:
                result2 = [x + y for x, y in zip(result, result2)]
                return result2


    is_prime(result)

    print(f"\nRound {d}\n")
    d += 1

    ee = {}
    myDict = {players[i]: result2[i] for i in range(0, len(players), 1)}
    sorted_tuple = sorted(myDict.items(), key=lambda x: x[1], reverse=False)
    ee.update(dict(sorted_tuple))
    num = 0

    for k, v in ee.items():
        num += 1
        m = str(k) + ' = ' + str(v)
        print(f"{num} " + m + " points")

    time.sleep(3)
