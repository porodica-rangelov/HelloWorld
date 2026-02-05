<div align="center">

# Sprint 1 - Nizovi i matrice u Pythonu

**Ovaj sprint sadrzi zadatke za vezbanje rada sa nizovima (listama) i matricama u Pythonu, ukljucujuci generisanje random brojeva i rad sa dijagonalama.**

</div>

---

## Uputstvo za izradu
- Svaki zadatak resavaj u posebnoj `.py` datoteci (npr. `sprint1_zadatak1.py`).
- Koristi jasna imena promenljivih i dodaj kratke komentare gde je potrebno.
- Testiraj program sa nekoliko razlicitih ulaza i velicina nizova/matrica.
- Za generisanje random brojeva koristi modul `random` (`import random`).

## Kratko uputstvo za koriscenje AI (ChatGPT i Codex)
> **Koristi AI kao pomocnika, ne kao zamenu.**

- Postavljaj konkretna pitanja (npr. "objasni kako radi random.randint" ili "proveri moj kod za matrice").
- Zadrzi svoje resenje i pokusaj da razumes svaki red koda koji dobijes.
- Ako AI predlozi kompletno resenje, prvo pokusaj sam, pa uporedi i pitaj gde gresis.

## Kompleksnost zadataka
- **[1]** - Lak zadatak (osnovne petlje i operacije)
- **[2]** - Srednji zadatak (kombinovanje vise koncepata)
- **[3]** - Tezi zadatak (ugnjezdene petlje, logika sa indeksima)

---

## Zadaci

### Task 1: Generisanje niza od N random integera [Kompleksnost: 1]
- [ ] Uneti broj N od korisnika
- [ ] Generisati niz od N random celih brojeva u opsegu od 1 do 100
- [ ] Ispisati generisani niz

**Uputstvo za resavanje:**
1. Koristiti `input()` za unos broja N i konvertovati ga u `int`
2. Importovati `random` modul na pocetku fajla
3. Napraviti praznu listu
4. Koristiti `for` petlju od 0 do N:
   - U svakoj iteraciji generisati random broj pomocu `random.randint(1, 100)`
   - Dodati broj u listu pomocu `append()`
5. Prikazati generisani niz

---

### Task 2: Trazenje min i max elementa u nizu od N random integera [Kompleksnost: 2]
- [ ] Generisati niz od N random celih brojeva (N unosi korisnik)
- [ ] Pronaci minimalni element bez koriscenja ugradjenih `min()`/`max()` funkcija
- [ ] Pronaci maksimalni element bez koriscenja ugradjenih funkcija
- [ ] Prikazati niz, minimum i maksimum

**Uputstvo za resavanje:**
1. Generisati niz od N random brojeva (kao u Task 1)
2. Inicijalizovati `minimum` i `maksimum` na prvi element niza (`niz[0]`)
3. Koristiti `for` petlju za prolazak kroz sve elemente niza:
   - Ako je trenutni element manji od `minimum`, azurirati `minimum`
   - Ako je trenutni element veci od `maksimum`, azurirati `maksimum`
4. Prikazati niz, pronadjeni minimum i maksimum

---

### Task 3: Obrtanje niza (reverse) bez ugradjenih funkcija [Kompleksnost: 1]
- [ ] Uneti N brojeva u listu
- [ ] Obrnuti redosled elemenata bez koriscenja `reverse()` ili `[::-1]`
- [ ] Prikazati originalni i obrnuti niz

**Uputstvo za resavanje:**
1. Napraviti listu od N brojeva (unos ili random generisanje)
2. Sacuvati kopiju originalne liste za prikaz
3. Koristiti `for` petlju sa dva indeksa (pocetak i kraj):
   - `i` krece od 0, `j` krece od poslednjeg indeksa
   - Zameniti `niz[i]` i `niz[j]`
   - Ponavljati dok se indeksi ne sretnu na sredini
4. Prikazati originalni i obrnuti niz

---

### Task 4: Prebrojavanje elemenata niza vecih od proseka [Kompleksnost: 1]
- [ ] Generisati niz od N random celih brojeva
- [ ] Izracunati prosek (aritmeticku sredinu) svih elemenata
- [ ] Prebrojati i ispisati koliko elemenata je vece od proseka

**Uputstvo za resavanje:**
1. Generisati niz od N random brojeva
2. Izracunati sumu svih elemenata koristeci `for` petlju
3. Podeliti sumu sa brojem elemenata da se dobije prosek
4. Ponovo proci kroz niz i brojati koliko elemenata je vece od proseka
5. Prikazati niz, prosek i broj elemenata vecih od proseka

---

### Task 5: Kreiranje i ispis matrice NxN sa random brojevima [Kompleksnost: 2]
- [ ] Uneti dimenziju matrice N
- [ ] Generisati matricu NxN sa random celim brojevima (1-50)
- [ ] Ispisati matricu u tabelarnom formatu (red po red)

**Uputstvo za resavanje:**
1. Uneti N od korisnika
2. Napraviti praznu listu koja ce predstavljati matricu (lista listi)
3. Koristiti ugnjezdene `for` petlje:
   - Spoljna petlja za redove (i od 0 do N)
   - Za svaki red napraviti praznu listu `red`
   - Unutrasnja petlja za kolone (j od 0 do N)
   - Generisati random broj i dodati u `red`
   - Dodati `red` u matricu
4. Ispisati matricu koristeci `for` petlju za svaki red

---

### Task 6: Suma elemenata na glavnoj dijagonali matrice [Kompleksnost: 2]
- [ ] Generisati matricu NxN sa random brojevima
- [ ] Ispisati matricu
- [ ] Izracunati i prikazati sumu elemenata na glavnoj dijagonali

**Uputstvo za resavanje:**
1. Generisati matricu NxN (kao u Task 5)
2. Ispisati matricu
3. Glavni dijagonala su elementi gde je indeks reda jednak indeksu kolone: `matrica[i][i]`
4. Koristiti `for` petlju od 0 do N:
   - Dodati `matrica[i][i]` na sumu
5. Prikazati elemente glavne dijagonale i njihovu sumu

---

### Task 7: Suma elemenata na sporednoj dijagonali matrice [Kompleksnost: 2]
- [ ] Generisati matricu NxN sa random brojevima
- [ ] Ispisati matricu
- [ ] Izracunati i prikazati sumu elemenata na sporednoj dijagonali

**Uputstvo za resavanje:**
1. Generisati matricu NxN (kao u Task 5)
2. Ispisati matricu
3. Sporedna dijagonala su elementi gde je: `matrica[i][N-1-i]`
   - Za i=0 uzimamo poslednju kolonu, za i=1 pretposlednju, itd.
4. Koristiti `for` petlju od 0 do N:
   - Dodati `matrica[i][N-1-i]` na sumu
5. Prikazati elemente sporedne dijagonale i njihovu sumu

---

### Task 8: Elementi iznad glavne dijagonale matrice [Kompleksnost: 3]
- [ ] Generisati matricu NxN sa random brojevima
- [ ] Ispisati matricu
- [ ] Pronaci i ispisati sve elemente iznad glavne dijagonale
- [ ] Izracunati njihovu sumu

**Uputstvo za resavanje:**
1. Generisati matricu NxN (kao u Task 5)
2. Ispisati matricu
3. Elementi iznad glavne dijagonale su oni gde je indeks kolone veci od indeksa reda: `j > i`
4. Koristiti ugnjezdene `for` petlje:
   - Spoljna petlja: `i` od 0 do N (redovi)
   - Unutrasnja petlja: `j` od `i+1` do N (kolone desno od dijagonale)
   - Dodati `matrica[i][j]` na sumu
5. Prikazati pronadjene elemente i njihovu sumu

---

### Task 9: Elementi ispod glavne dijagonale matrice [Kompleksnost: 3]
- [ ] Generisati matricu NxN sa random brojevima
- [ ] Ispisati matricu
- [ ] Pronaci i ispisati sve elemente ispod glavne dijagonale
- [ ] Izracunati njihovu sumu

**Uputstvo za resavanje:**
1. Generisati matricu NxN (kao u Task 5)
2. Ispisati matricu
3. Elementi ispod glavne dijagonale su oni gde je indeks reda veci od indeksa kolone: `i > j`
4. Koristiti ugnjezdene `for` petlje:
   - Spoljna petlja: `i` od 1 do N (redovi, krecemo od 1 jer prvi red nema elemente ispod dijagonale)
   - Unutrasnja petlja: `j` od 0 do `i` (kolone levo od dijagonale)
   - Dodati `matrica[i][j]` na sumu
5. Prikazati pronadjene elemente i njihovu sumu

---

### Task 10: Transponovanje matrice [Kompleksnost: 3]
- [ ] Generisati matricu NxN sa random brojevima
- [ ] Ispisati originalnu matricu
- [ ] Transponovati matricu (redovi postaju kolone i obrnuto) bez ugradjenih funkcija
- [ ] Ispisati transponovanu matricu

**Uputstvo za resavanje:**
1. Generisati matricu NxN (kao u Task 5)
2. Ispisati originalnu matricu
3. Kreirati novu praznu matricu NxN za rezultat
4. Koristiti ugnjezdene `for` petlje:
   - Spoljna petlja: `i` od 0 do N
   - Unutrasnja petlja: `j` od 0 do N
   - `nova_matrica[j][i] = matrica[i][j]` (zamena redova i kolona)
5. Prikazati originalnu i transponovanu matricu
6. Proveriti: prvi red originalne matrice treba da bude prva kolona transponovane

---

## Napomene
- Za sve zadatke sa matricama, koristiti isti pristup za generisanje matrice (Task 5).
- Indeksiranje u Pythonu pocinje od 0, sto je bitno za rad sa dijagonalama.
- Koristiti `random.seed()` ako zelis da dobijes iste random brojeve pri svakom pokretanju (korisno za testiranje).
- Preporuka: prvo resiti Task 1 i Task 5 jer su osnova za ostale zadatke.
