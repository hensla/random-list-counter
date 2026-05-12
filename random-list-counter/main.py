import random
lista = []

for i in range(10):
    a = random.randint(1, 10)
    lista.append(a)

n = int(input("numero: "))

print(f"seu numero ({n}) apareceu {lista.count(n)} vezes")
print(lista)