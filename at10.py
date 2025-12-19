num = int(input("Digite um numero: "))
maior = num
menor = num

for i in range(9):
    num = int(input("Digite um numero: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(maior)
print(menor)
