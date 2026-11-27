while True:
    print("Tee valik: ")

    print("1. Sisestatakse 15 arvu. for kasutades")
    print("2. Sisestatakse 15 arvu. while kastades")
    print("3. Sisestatakse 15 arvu. while True ja break kasutades")
    print("4. Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A. for kasutades")
    print("5. Sisestatakse 8 arvu. for kasutades")
    print("6. Sisestatakse 8 arvu. while kasutades")
    print("7. Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20. for kasutades")
    print("8. Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20. while kasutades")
    print("9. Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast. for kasutades")
    print("10. Klaviatuurilt sisestatakse N arvu. for kasutades")

    valik = input("Vali tegevus: ")
    if valik == "0":
        break
    elif valik == "1":
        # 1. Sisestatakse 15 arvu.
        # Määrata, mitu neist on täisarvud.
        #for kasutades
        for i in range(15):
            try:
                arv=float(input(f"{i+1}. arv: "))
                if arv.is_integer():
                    print(f"{arv} ei ole täisarv.")
                else:
                    print(f"{arv} ei ole täisarv.")
            except ValueError:
                    print("Palun sissetage arv.")
    elif valik == "2":  
        #while kasutades
        i = 0
        while i < 15:
            try:
                arv = float(input(f"{i + 1}. arv: "))
                if arv.is_integer():
                    print(f"{arv} on täisarv")
                else:
                    print(f"{arv} ei ole täisarv")
            except ValueError:
                    print("Palun sissetage arv.")
            i += 1
    elif valik == "3":
        #while True ja break kasutades
        i = 0
        while True:
            try:
                arv = float(input(f"{i + 1}. arv: "))
                if arv.is_integer():
                    print(f"{arv} on täisarv")
                else:
                    print(f"{arv} ei ole täisarv")
                i += 1 #arvu lugumine, ainult siis kui sisestus on õige
                if i==15:
                   break
            except ValueError:
                    print("Palun sisestage arv.")
    elif valik == "4":
        # 2. Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.
        #for kasutades
            try:
                A=int(input("Sisesta arv A: "))
                summa = 0
                for i in range(1, A + 1):
                    summa += i
                    print(f"Summa vahemikus 1 kuni {A} on {summa}.")
            except ValueError:
                    print("Palun sisestage täisarv. ")
    elif valik == "5":
        # 3. Sisestatakse 8 arvu.
        # Leida nende korrutis (ainult positiivsete arvude puhul).
        korrutis=1
        for i in range(8):
            try:
                arv = float(input(f"{i + 1}. arv: "))
                if arv > 0:
                    korrutis *= arv
            except ValueError:
                    print("Palun sisestage arv.")
                    print(f"Positiivsete arvude korrutis on {korrutis}.")
    elif valik == "6":
        #while kasutades
        korrutis = 1
        i = 0

        while i < 8:
            try:
                arv = float(input(f"{i + 1}. arv: "))
                if arv > 0:
                    korrutis *= arv
            except ValueError:
                    print("Palun sisestage arv.")
        i += 1

        print(f"Positiivsete arvude korrutis on {korrutis}.")
    elif valik == "7":
        # 4. Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.
        for i in range(10, 21):
            print(f"{i} ruut on {i ** 2}")
        #while
        i = 10
        while i <= 20:
            print(f"{i}^2 = {i**2}")
            i += 1
    elif valik == "8":
        #5. Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
        # N väärtus sisestatakse klaviatuurilt.
        #for kasutades
        N = int(input("Sisesta arvude kogus: "))
        summa = 0

        for i in range(N):
            try:
                arv = float(input(f"{i + 1}. arv: "))
                if arv < 0:
                    summa += arv
            except ValueError:
                    print("Palun sisestage arv.")

        print(f"Negatiivsete arvude summa on {summa}.")

        #6. Klaviatuurilt sisestatakse N arvu.
        # Koosta programm, mis määrab sisestatud arvude seast:

        # negatiivsete arvude arvu,

        # positiivsete arvude arvu,

        # nullide arvu.
        # (N väärtus sisestatakse klaviatuurilt.)
    elif valik == "9":
        try:
            N = int(input("Sisesta arvude kogus N: "))
            negatiivsed = 0
            positiivsed = 0
            nullid = 0
            for i in range(N):
                try:
                    arv = float(input(f"{i + 1}. arv: "))
                    if arv < 0:
                        negatiivsed += 1
                    elif arv > 0:
                        positiivsed += 1
                    else:
                        nullid += 1
                except ValueError:
                    print("Palun sissesta arv.")
            print(f"Negatiivsete arvude arv: {negatiivsed}")
            print(f"Positiivsete arvude arv: {positiivsed}")
            print(f"Nullide arv: {nullid}")
        except ValueError:
                    print("Palun sissestage arv.")

#Mul ei jätkunud aega viie ülesande tegemiseks :(