

laikāNenodotas = input("Vai ir nodotas iepriekšējās grāmatas? Ievadiet Jā vai Nē ")
if laikāNenodotas == "Nē":
    print('Tas nozīmē, ka jums ir laikā nenodotas grāmatas un parāds, šobrīd nevarat izņemt grāmatu. ')
    raise ValueError ('Nevarat veikt turpmāku darbību ') #Tiek parādīts Error, kas norāda, ka turpmāko darbību izmantotājs nevar veikt, jo nav nodevis grāmatas
if laikāNenodotas == 'Jā': 
    print('Jums ir iespēja saņemt citu izdevumu, ko piedāvā bilbiotēka. ')




Pieprasīt = input('Vai vēlaties izņemt pieprasītu izdevumu? Ievadiet Jā vai Nē ') #Tiek pieprasīts programmas izmantotājam, ievadīt Jā vai Nē, lai veiktu turpmākās darbības 
if Pieprasīt == 'Jā':
    print("Varam izsniegt uz divam dienām ")
else:
    print("...")


Grāmatas = input('Vai tā ir grāmata, kas nav pieprasīto sarakstā? Ievadiet Jā vai Nē ')
if Grāmatas == "Jā": 
    print("Izdevumu ir iespēja saņemt uz 28 dienām personālam un 14 dienām studentiem. ")
else: 
    print("...")


    
Žurnāli = input("Vai izvelētais izdevums ir žurnāls, kas nav pieprasīto sarakstā? Ievadiet Jā vai Nē ")
if Žurnāli == 'Jā':
    print("Ir iespēja saņemt uz 7 dienām ikvienam. ")
else: 
    print("...")


print("Sazinaties ar bibliotekāri, lai sarunātu izdevuma saņemšanas brīdi! ")




















