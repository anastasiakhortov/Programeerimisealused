# Loo uus projekt.
# Kopeeri antud kood failisse.
# Otsi ja paranda programmis vead.
# Lisa kommentaar, kus kirjelda, mis parandatud oli.

 
# Kood:
# # print("Kolmnurga kontroll")
# # a=input("Sisesta 1. külje pikkus => ")
# # b=float(input("Sisesta 2. külje pikkus => "))
# # c=float(input("Sisesta 3. külje pikkus => "))
# # if a+b>c or a+c>b or b+c>a:
# #     print("Kolmnurk on olemas")
# #     if a=b=c
# #         print("Kolmnurk on võrdkülgne")
# #     else if a==b or b==c:
# #         print("Kolmnurk on võrdhaarne")
# #     else:
# #     print("Kolmnurk on erikülgne")
# # else:
# #     print("Sellist kolmnurka ei ole olemas")
# # print()
# # print("Hinde arvutamine")
# # punktid=int(input("Sisesta punktide arv (0-100) => "))
# # if punktid<0 and punktid>100:
# #     print("Vigane punktide arv")
# # elif punktid>=50:
# #     print("Hinne: 3")
# # elif punktid>=75:
# #     print("Hinne: 4")
# # elif punktid>=90:
# #     print("Hinne: 5")
# # else:
# #     print("Hinne: 2")
# # print()
# # print("Pileti hind")
# # vanus=int(input("Sisesta oma vanus => "))
# # if vanus<7:
# #     print("Pilet on tasuta")
# # elif 7<=vanus<=18 or vanus=>65:
# #     print("Pileti hind on 3 €")
# # else:
# #     print("Pileti hind on 6 €")
# Programmi tulemus:
 
# Kolmnurga kontroll
# Sisesta 1. külje pikkus => 3
# Sisesta 2. külje pikkus => 4
# Sisesta 3. külje pikkus => 5
# Kolmnurk on olemas
# Kolmnurk on erikülgne

# Hinde arvutamine
# Sisesta punktide arv (0-100) => 82
# Hinne: 4

# Pileti hind
# Sisesta oma vanus => 70
# Pileti hind on 3 €
# Lisaülesanne:

# Muuda programmi nii, et alguses kuvatakse menüü ja kasutaja valib, millist osa käivitada:
 
# Vali programm:
# 1 - Kolmnurga kontroll
# 2 - Hinde arvutamine
# 3 - Pileti hind
# Sisesta valik (1-3) =>
# Käivitub ainult valitud osa. Kui kasutaja sisestab midagi muud kui 1, 2 või 3, kuvatakse teade Vigane valik.

# Lisa kolmnurga osasse kontroll, kas kolmnurk on täisnurkne (Pythagorase teoreem).
# Kolmnurga osa ei tohi lubada sisestada nulli või negatiivset külje pikkust.
# Lisaülesande tulemus (näide):

 
# Vali programm:
# 1 - Kolmnurga kontroll
# 2 - Hinde arvutamine
# 3 - Pileti hind
# Sisesta valik (1-3) => 1
# Kolmnurga kontroll
# Sisesta 1. külje pikkus => 3
# Sisesta 2. külje pikkus => 4
# Sisesta 3. külje pikkus => 5
# Kolmnurk on olemas
# Kolmnurk on erikülgne
# Kolmnurk on täisnurkne

#MINU TÖÖ

print("Vali programm:")
print("1 - Kolmnurga kontroll")
print("2 - Hinde arvutamine")
print("3 - Pileti hind")

valik=input("Sisesta valik (1-3) => ")
try:
    if valik== "1":
        print("Kolmnurga kontroll") #parandasin jutumärgid
        a=float(input("Sisesta 1.külje pikkus => ")) #puudus float
        b=float(input("Sisesta 2.külje pikkus => "))
        c=float(input("Sisesta 3.külje pikkus => ")) #puudus üks sulg
        if a <= 0 or b <= 0 or c <= 0: # lisasin kontrolli et küljed ei oleks 0 või negatiivne
            print("Vigane külje pikkus")
        elif a+b > c and a+c > b and b+c > a: # muutsin "or" ja "and". ja lisasin kooloni
            print("Kolmnurk on olemas")
            if a == b == c:
                print("Kolmnurk on võrdkülgne")
            elif a == b or b == c or a == c: # muutsin else if ja elif. lisasin a == c
                print("Kolmnurk on võrdhaarne")
            else:
                print("Kolmnurk on erikülgne") # parandasin taande
            küljed = sorted([a, b, c]) # lisasin täisnurkse kolmnurga kontrolli. me ei oleme see õpinnud tundides, aga ma olen see ise õppinud. Või oleme, aga mind ei olnud tunnis
            x, y, z = küljed

            if abs(x**2 + y**2 - z**2) < 0.000001: 
                print("Kolmnurk on täisnurkne")
        else:
            print("Sellist kolmnurka ei ole olemas")

    elif valik == "2":
        print("Hinde arvutamine")
        punktid = int(input("Sisesta punktide arv (0-100) => "))

        if punktid < 0 or punktid > 100: # muutsin "and" ja "or"
            print("Vigane punktide arv")
        elif punktid >= 90: # parandasin tingimuste jarjekorda
            print("Hinne: 5")
        elif punktid >= 75:
            print("Hinne: 4")
        elif punktid >= 50:
            print("Hinne: 3")
        else:
            print("Hinne: 2")
    elif valik == "3":
        print("Pileti hind")
        vanus = int(input("Sisesta oma vanus => "))

        if vanus < 0: # lisasin kontrolli et vanus ei oleks negatiivne
            print("Vigane vanus")
        elif vanus < 7:
            print("Pilet on tasuta")

        elif 7 <= vanus <= 18 or vanus >= 65: # muutsin "=>" ja ">="
            print("Pileti hind on 3 €")
        else:
            print("Pileti hind on 6 €") # lisasin kooloni ja puuduva sulu

    else:
        print("Vigane valik")

except ValueError: # lisasin try except et programm ei annaks error
    print("Vigane sisend! Sisesta arv.")