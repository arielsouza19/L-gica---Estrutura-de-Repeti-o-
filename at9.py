soma_par = 0
soma_impar = 0

for i in range(10):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        soma_par += num
    else:
        soma_impar += num

print(soma_par)
print(soma_impar)
