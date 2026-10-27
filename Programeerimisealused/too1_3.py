# import calendar
# from datetime import *
# from calendar import *   #monthrange
from math import *

# # Ülesanne 1

# tana=date.today()
# print(f"Täna on {tana}")

# # 27/12/2022
# tana1 = tana.strftime("%d/%m/%Y")
# print(f"Täna on {tana1}")

# # December 27, 2022
# tana2 = tana.strftime("%B %d, %Y")
# print(f"Täna on {tana2}")

# # 12/27/22
# tana3 = tana.strftime("%m/%d/%y")
# print(f"Täna on {tana3}")

# # Dec-27-2022
# tana4 = tana.strftime("%b-%d-%Y")
# print(f"Täna on {tana4}")

# # Omadused day, month, year kasutatakse päeva, kuu ja aasta parameetri leidmiseks date klassist.
# # Arvuta mitu päeva on jäänud kuu lõpuni, aasta lõpuni.
# # Arvuta oma vanus aastates, kuudes ja päevades.
# print("Täna on", tana.day)
# print("päev, kuu number on", tana.month)
# print("ja aasta on", tana.year)

# kuulõpuni=monthrange(tana.year,tana.month)[1] - tana.day
# oktoobris on 31 päeva, 31-27=4 päeva jäänud
# # print("Kuu lõpuni on jäänud", kuulõpuni, "päeva.")
# # aastalõpuni=(date(tana.year, 12, 31) - tana).days
#days -> 65 päeva jäänud
# # print("Aasta lõpuni on jäänud", aastalõpuni, "päeva.")
# # sünnipäev=date(2010, 4, 19)
# # vanus=aastalõpuni//365
# # print("Oled", vanus, "aastat, ")
# # print((aastalõpuni%365)//30, "kuud ja")
# # print((aastalõpuni%365)%30, "päeva vana.")

# Ülesanne 2
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.
# # print("3 + 8 / (4 - 2) * 4=", 3 + 8 / (4 - 2) * 4)
# # print("3 + 8 / 4 - 2 * 4=", 3 + 8 / 4 - 2 * 4)
# # print("(3 + 8) / 4 - 2 * 4=", (3 + 8) / 4 - 2 * 4)

# Ülesanne 3
# Ruudu sees asub ring. Ringi raadius on R.
# Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt

try:
    R=float(input("Sisesta ringi raadius: "))
    print("Ruudu pindala:", R++2)
    print("Ruudu ümbermõõt:", 4*R)
    print("Ringi pindala:", 3.14*R**2)
    print("Ringi ümbermõõt:", 2*3.14*R)
except :
    print("Valed andmed")

# Ülesanne 4
# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu: kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.

# Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses sisukate nimedega muutujatele. Kuna ümbermõõdu arvutamiseks tuleb kasutada  PI-d (3,14...), siis võid selle (umbkaudse) väärtuse otse programmi kirjutada.  
# Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda (teisendamised, ümardamise täpsus jne). Võimalusel võrrelge tulemusi teistega. Kui on erinevusi, leidke ühiselt põhjused.
# Kas programm on piisavalt hästi kirjutatud, et algandmete muutumise korral (näiteks juhul, kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) on parandusi selge ja lihtne teha?
