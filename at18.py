op = 0

while op != 3:
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Sair")

    op = int(input("Escolha: "))

    if op == 1:
        a = int(input("Digite um numero: "))
        b = int(input("Digite outro numero: "))
        print(a + b)

    elif op == 2:
        a = int(input("Digite um numero: "))
        b = int(input("Digite outro numero: "))
        print(a - b)
