import random

angka_rahasia = random.randint(1, 20)
kesempatan = 5

while kesempatan > 0:
    tebakan = int(input("Tebak angka 1-20 yang kalah pacar dapa: "))

    if tebakan == angka_rahasia:
        print("Benar! Kamu menang 🎉")
        break
    elif tebakan > angka_rahasia:
        print("Kebesaran 😅")
    else:
        print("Kekecilan 😁")

    kesempatan -= 1
    print("Sisa kesempatan:", kesempatan)

if kesempatan == 0:
    print("Kamu kalah ❌ Angkanya adalah:", angka_rahasia)
    print  ("awokawokawok pacar dapa")