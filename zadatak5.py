lista = []

for i in range(10):
    broj = int(input("Unesi broj: "))
    lista.append(broj)
#ovaj deo koda nas 10 puta pita da unesemo broj po zelji
zbir = 0
for x in lista:
    zbir += x
#ovaj deo koda izracunava zbir elemenata
aritmeticka_sredina = zbir / len(lista)

print("Lista:", lista)
print("Zbir elemenata:", zbir)
print("Aritmetička sredina:", aritmeticka_sredina)
#ovaj deo izracunava aritmeticku sredinu i printuje listu, zbir elemenata i aritmeticku sredinu