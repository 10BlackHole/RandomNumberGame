import random
# from src import val

def val():
    n = int(input("Escoge una cota superior para adivinar el número: "))
    while (n<=0):
        print("Debe ser un número mayor a 0")
    return n

def cota():
    print("Quieres escoger tú mismo la cota superior?. Por defecto es 10")
    cota= str(input("(Y) si es afirmativo o (N) si es negativo: "))
    return cota

def guess(x):
    intentos = []
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        intentos.append(0)
        guess = int(input(f"Adivina el número entre 1 y {x}: "))
        if (guess < random_number):
            print("Muy bajo. Inténtalo de nuevo")
        elif (guess > random_number):
            print("Muy alto. Inténtalo de nuevo")
    print(f"Felicidades. Has adivinado el número {random_number} !!!")
    print(f"Te ha llevado {len(intentos)} intentos.")

# def computer_guess(x):
    # return a
guess(val())

