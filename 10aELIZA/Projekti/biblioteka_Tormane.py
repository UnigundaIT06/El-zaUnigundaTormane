pieprasiti = ['žurnāls', ' grāmata']


nenodotas_Dotas = input("Labdien, vai pie jums atrodas laikā nenodots izdevums? (Jā/Nē) :")
if nenodotas_Dotas == "Nē":
    print("Jūs varat turpināt izdevuma pieprasījumu. ")
while nenodotas_Dotas == "Jā": 
    print ("Jūs nevarat turpināt izdevumu pieprasījumu. ")
    break
else: 
    print ("Vai šis vēlamais izdevums ir (pieprasīts/nepieprasīts)? ")
pieprasiti = input(" ")
if pieprasiti == "pieprasīts":
    print("Jums pienākas izdevums uz 2 dienām. ")
elif pieprasiti == "nepieprasīts":
    print("Vai jūs vēlaties saņemt žurnālu vai grāmatu? (Žurnālu/Grāmatu): ")
gramata_žurnals = input('')
if gramata_žurnals == "Žurnālu":
    print("Jums ir iespēja saņemt šo izdevumu uz 7 dienām! ")
elif gramata_žurnals == 'Grāmatu':
    print("Vai jūs esat students, vai personāls? (Personāls/Students)")
student_worker = input(" ") 
if student_worker == "Personāls":
    print("Jums ir iespēja saņemt šo izdevumu uz 28 dienām, vai to vēlaties? (Jā/Nē)")
    ja = input("")
    if ja == "Jā":
        print("24h laikā bibliotēka sazināsies ar jums! ")
    else: 
        print("Sākat darbības no jauna!")

elif student_worker == "Students":
    print("Jums ir iespēja saņemt šo izdevumu uz 14 dienām, vai to vēlaties? (Jā/Nē)" )
    ja = input('')
    if ja == "Jā":
        print("24h laikā bibliotēka sazināsies ar jums! ")
    else: 
        print("Sākat darbības no jauna!")




















