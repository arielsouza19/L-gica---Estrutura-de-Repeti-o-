import random

num = random.randint(1, 20)
palpite = 0

while palpite != num:
    palpite = int(input("Digite um numero: "))

print("Acertou")
