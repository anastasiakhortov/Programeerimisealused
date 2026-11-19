#Ülesanne 1. Juku
# Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, muidu teatatakse, et täna kinno ei minda.
# Programm peab Juku ära tundma ka siis, kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, lisa märkus „Ära karju, Juku!“.
eesnimi=input("Sisesta eesnimi ")
if eesnimi.lower() == "juku":
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
    elif eesnimi.islower():
        print("Ära sissesta, Juku!")
    # Kui kinno läheb Juku, küsi tema vanus ja otsusta, millist piletit on vaja osta:
    vanus=input(f"Kui vana on {eesnimi}? ")
    if vanus.isdigit():
        vanus=int(vanus)
        if 0<vanus<6:
            pilet="tasuta pilet"
        elif 6<=vanus<14:
            pilet="lapsepilet"
        elif 14<=vanus<65:
            pilet="täispilet"
        elif 65<=vanus<100:
            pilet="sooduspilet"
        else:
            pilet="tundmatu pilet"
        print(f"{eesnimi} vajab {pilet}. ")
    else:
        print("Viga andmedega")
else:
    print("Täna kinno ei minna")

#2. Pinginaabrid
#Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. Kui mõnes nimes on numbreid või muid märke, kuva veateade.
#Otsusta ise, kuidas „pinginaabrid“ määratakse, näiteks juhuslikult või nimede algustähtede järgi.
#Kasuta: isalpha(), capitalize()
pinginaabrid=["Anastasia","Anna"]
nimi1=input("Sisesta nimi: ")
nimi2=input("Sisesta nimi: ")


# 3.Remont
# Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav, küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
# Kasuta: float(), lower() (vastuse „Jah“, „JAH“, „jah“ äratundmiseks), round()

# # try:
# #     pikkus=float(input("Sisesta pikkus: "))
# #     laius=float(input("Sisesta laius: "))
# #     pindala=round(pikkus*laius,2) #ümardamine
# #     print(f"Pindala on {pindala}")
# #     remont=input("Kas soovid remonti teha? (jah/ei)").lower() #tähed on väikesed
# #     if remont=="jah":
# #         print("Teeme remonti!")
# #         try:
# #             rm_hind=float(input("Sisesta ruutmetri hind: "))
# #             hind=round(pindala*rm_hind,2)
# #             print(f"Põranda vahetamise hind on {hind} €")
# #             ise=input("Kas teeb remondi is?(jah/ei)").lower()
# #             if ise=="jah":
# #                 print(f"Põranda vahetamise hind on {hind} €")
# #             else:
# #                 try:
# #                     töö_hind=float(input("Töö hind: "))
# #                     koguhind=round(hind+pindala*töö_hind,2)
# #                     print(f"Remondi koguhind koos tööga on {koguhind}")
# #                 except ValueError:
# #                     print("Tööhind on ujukomarv")
# #         except ValueError:
# #             print("Viga: ruutmeetri hind on arv")
# #     else:
# #         print("Remonti ei tehta!")
# # except ValueError:
# #     print("Viga: kasuta numbreid pikkuse ja laiuse sisestamiseks")

#ÜLESANNE 4. Allahindlus
# Küsi toote alghind. Kui alghind on üle 700 euro, arvuta hind 30% soodustusega. Muul juhul jääb hind samaks. Kuva lõplik hind kahe komakohaga.

# # try:
# #     alghind = float(input("Sisesta toote alghind (€): "))

# #     if alghind > 700:
# #         lõplik_hind = alghind * 0.7
# #     else:
# #         lõplik_hind = alghind

# #     print(f"Toote lõplik hind on {lõplik_hind:.2f} €.")

#ÜLESANNE 5. Temperatuur
# Küsi toatemperatuur ja teata, kas see on üle 18 kraadi (soovitatav toasoojus talvel). Temperatuur võib olla ka negatiivne või kümnendarv, seega kontrolli sisendit try/except abil.

# # try:
# #     temperatuur = float(input("Sisesta toatemperatuur: "))
# #     if temperatuur > 18:
# #         print("Temperatuur on üle 18 kraadi (piisavalt soe).")
# #     else:
# #         print("Temperatuur on 18 kraadi või madalam (jahe).")
# # except ValueError:
# #     print("Viga! Palun sisesta korrektne arv.")

#ÜLESANNE 6. Pikkus
# Küsi inimese pikkus sentimeetrites ja teata, kas ta on lühike, keskmise pikkusega või pikk. Piirid pane ise paika ja kirjuta need programmi alguses kommentaarina.

# Piirid:
# lühike: alla 165 cm
# keskmine: 165 - 180 cm
# pikk: üle 180 cm

# pikkus = int(input("Sisesta inimese pikkus sentimeetrites: "))

# if pikkus < 165:
#     print("Inimene on lühike.")
# elif pikkus <= 180:
#     print("Inimene on keskmise pikkusega.")
# else:
#     print("Inimene on pikk.")

#ÜLESANNE 7. Pikkus ja sugu
# Täienda ülesannet 6: küsi lisaks sugu. Meestele ja naistele kehtivad erinevad piirid. Tingimusplokid võivad olla üksteise sees.
# Sugu võib sisestada mis tahes kujul (M, m, mees, MEES). Programm peab selle ära tundma.
# Kui sugu on sisestatud valesti, kuva veateade.
# Kasuta: pesastatud if-laused, lower()

# Piirid meestele: lühike < 170 cm, keskmine 170-185 cm, pikk > 185 cm
# Piirid naistele: lühike < 160 cm, keskmine 160-175 cm, pikk > 175 cm
# sugu = input("Sisesta sugu (M/mees või N/naine): ").strip().lower()
# pikkus = int(input("Sisesta inimese pikkus sentimeetrites: "))

# if sugu == "m" or sugu == "mees":
#     if pikkus < 170:
#         print("Mees on lühike.")
#     elif pikkus <= 185:
#         print("Mees on keskmise pikkusega.")
#     else:
#         print("Mees on pikk.")
# elif sugu == "n" or sugu == "naine":
#     if pikkus < 160:
#         print("Naine on lühike.")
#     elif pikkus <= 175:
#         print("Naine on keskmise pikkusega.")
#     else:
#         print("Naine on pikk.")
# else:
#     print("Viga! Tundmatu sugu.")

#ÜLESANNE 8. Poes
# Küsi kasutajalt iga toote kohta eraldi, kas ta soovib seda osta: piim, sai, leib ja vähemalt kaks toodet veel.
# Toodete hinnad loo juhuslikult moodulist random, näiteks round(random.uniform(0.5, 3), 2).
# Kui kasutaja soovib toodet osta, küsi kogus. Kontrolli, et kogus on täisarv (isdigit()).
# Lõpus kuva tšekk: iga ostetud toote nimi, kogus, hind ja summa ning kõige all kogusumma.

from random import *
summa=0
arve="Toode   Kogus   Hind   Kokku\n"
valik=input("Kas soovid osta piima? (jah/ei): ")
if valik.lower()=="jah":
    kogus=input("Kui palju piima soovid osta (täisarv): ")
    if kogus.isdigit():
        kogus=int(kogus)
        piim_hind=round(uniform(0.5, 3), 2)
        print(f"Piima hind on {piim_hind} eurot.")
        summa+=round(kogus*piim_hind,2)
        print(f"Piima kogusumma on {summa} eurot. ")
        arve+=f"piim   {kogus}   {piim_hind}€   {kogus*piim_hind}€\n"
    else:
        print("Viga: vale hind!")
else:
    print("Selge: Piima ei taha")
print(f"Kogusumma on:{summa} eurot.")
