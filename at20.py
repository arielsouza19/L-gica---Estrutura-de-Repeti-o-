soma = 0
cont = 0
pares = 0

num = int(input("Digite um numero: "))
maior = num
menor = num

while num != 0:
    soma += num
    cont += 1

    if num % 2 == 0:
        pares += 1

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    num = int(input("Digite um numero: "))

media = soma / cont

print(cont)
print(media)
print(maior)
print(menor)
print(pares)
