recepteS = ["Āboli", "Cukurs", "Ūdens", "Citrons", "Mandeļu ekstrakts", "Kanēlis"]

print("Labdien! Esmu interaktīvais palīgs ievārījumu vārīšanā! > ") 
ja = input("Vai esat gatavs/a darbam? (JĀ/NĒ) > ")
if ja == "NĒ":
    print("Skumji! Gaidīšu jūs atpakaļ vēlāk. :( ")
    exit()
elif ja == "JĀ":
    print("Lieliski! Saāksim gatavot, bet vispirms sagatavošanās!")

print("Receptei nepieciešami šādi produkti: \nĀboli, \nCukurs, \nŪdens, \nCitrons, \nMandeļu ekstrakts, \nkanēlis")

recepte = input("Vai jums jau ir viss sagādāts receptei? (J/N)>")
if recepte == "N":
    print("Kādas sastāvdaļas nepieciešamas? ")
    neSastavdalas = input(" ")
   
if neSastavdalas == "N":
        print("Nepieciešams doties uz veikalu.") #NEPIECIEŠAMAS CENAS
elif neSastavdalas == "Cukurs":
        print("Cukura cena šobrīd veikalā ir > 1.35 euro",  )
elif neSastavdalas == "Citrons":
        print("Citrona cena šobrīd veikalā > 2.29 euro ")
elif neSastavdalas == "Kanēlis":
        print("Kanēļa cena šobrīd veikalā > 1.19 euro " )
elif neSastavdalas == "Mandeļu ekstrakts":
        print("Mandeļu ekstrakta cena šobrīd veikalā > 2.00 euro")
elif recepte == "J":
    print('Lieliski!')

ml = input("Cik ml mandeļu ekstrakts jums ir? > ")
if ml > 0: 
      print("Nepie")


svars = int(input("Cik KG āboli jums ir pieejami? > "))
if svars > 1:
     print ("Lieliski! Jums ir nepieciešamais daudzums, lai savārītu ievārījumu. > ", svars,"kg")
     print ("Iespējams, ka vajadzēs piemērot sastāvdaļu vajadzīgos gramus - ābolu kilogramiem! ") 
elif svars < 1: 
     print("Jums nav vajadzīgais kg skaits! :( ", "\nVarbūt pajautājiet mazbērniem, lai salasa?")







