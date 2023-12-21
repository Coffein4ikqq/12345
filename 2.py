import random

def game():
    n = random.randint(4, 30)
    turn = 1 
    while n > 0:
        print("Осталось камней:", n)
        if turn == 1:
            taken = random.randint(1, 3)
            print("Программа взяла", taken, "камней.")
        else:
            taken = int(input("Ваш ход (введите число от 1 до 3): "))
            while taken < 1 or taken > 3:
                taken = int(input("Некорректный ход. Введите число от 1 до 3: "))
            print("Вы взяли", taken, "камней.")
        n -= taken
        turn = 3 - turn 
    if turn == 1:
        print("Вы победили!")
    else:
        print("Бот победил!")
game()
