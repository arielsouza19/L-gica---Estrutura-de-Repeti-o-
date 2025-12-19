a = int(input("Digite A: "))
b = int(input("Digite B: "))

i = a + 1
while i < b:
    if i % 2 != 0:
        print(i)
    i += 1
