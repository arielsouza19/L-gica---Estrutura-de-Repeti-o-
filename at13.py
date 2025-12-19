n = int(input("Digite um numero: "))
i = 1
div = 0

while i <= n:
    if n % i == 0:
        div += 1
    i += 1

if div == 2:
    print("Primo")
else:
    print("Nao primo")
