print("Dobrodosli u sume prvih 10 brojeva")

suma = 0

for i in range(1, 11):
    suma += i

print(suma)

suma = 0
brojac = 0
n = 1

while brojac < 10:
    if n % 2 == 0:
        suma += n
        brojac += 1
    n += 1

print(suma)

suma = 0
brojac = 0
n = 1

while brojac < 10:
    if n % 2 != 0:
        suma += n
        brojac += 1
    n += 1

print(suma)