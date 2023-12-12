merijumi = {
    "1.decembris": 10,
    "2.decembris": 5,
    "3.decembris": 0,
    "4.decembris": 7,
    "5.decembris": 8,
    "6.decembris": 1,
    "7.decembris": 3

}

temp_aprekinasana = merijumi

datuma_ievade = input("Ievadiet datumu(piemēram, '1.decembris'): ")
if datuma_ievade in merijumi: 
    print(datuma_ievade,"temperatūra Celsija skalā ir: ")
    print("*****")
    print(merijumi.keys(),"temperatūra Fārenheita skalā ir: " )
elif datuma_ievade not in merijumi:
    for datuma_ievade in range(0,datuma_ievade):
        print(datuma_ievade)


else:
    print()