import random

def val():
    n = int(input("Escoge una cota superior para adivinar el número: "))
    while (n<=0):
        print("Debe ser un número mayor a 0")
    return n

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input(f"Adivina el número entre 1 y {x}: "))
        if (guess < random_number):
            print("Muy bajo. Inténtalo de nuevo")
        elif (guess > random_number):
            print("Muy alto. Inténtalo de nuevo")
    print(f"Felicidades. Has adivinado el número {random_number}")

guess(val())
