def val():
    n = int(input("Escoge una cota superior para adivinar el número: "))
    while (n<=0):
        print("Debe ser un número mayor a 0")
    return n
