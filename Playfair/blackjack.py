# See on Playfair messi blackjacki töötoa kood.
import random

# kasutaja_nimi = input("Tere, mis on teie nimi? ")

# print("Tere, " + kasutaja_nimi + ", mängime blackjacki!")

kasutaja_punktid = 0
arvuti_punktid = 0

suvakas_kaart = random.randint(1, 13)


while True:
    sisend = input("Kas soovid võtta uue kaardi? Vastasel juhul mäng lõppeb. (Y/N)").lower()
    print("Sul on " + str(kasutaja_punktid) + " punkti.")

    if sisend == "y":
        print("Võtsite uue kaardi!")
        kasutaja_punktid += suvakas_kaart
    elif sisend == "n":
        print("Mängu lõpp!")
        break
    else:
        print("Vale sisend.")


if kasutaja_punktid > 21:
    print("Kaotasid, sul oli " + kasutaja_punktid + "punkti.")
elif kasutaja_punktid == arvuti_punktid:
    print("Viik")
elif kasutaja_punktid > arvuti_punktid & kasutaja_punktid <= 21:
    print("Võitsid")
