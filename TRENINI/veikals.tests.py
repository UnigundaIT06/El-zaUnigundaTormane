stop = '0'
ceks = "Iepirkšanās čeks: " #Izveidots, lai katru reizi nebūtu jāvada teksts
summa_bez_atlaides = 0.0
kopsumma = 0.9 #galējā summa

while stop == '0':
    ceks
    
    precu_skaits = int(input("Ievadiet preču skaitu: "))
    if precu_skaits < 0: #ja mazāks par 0, tad programma beidzas
        exit()
    produkts = input("Ievadiet preces nosaukumu :  ")
    produkta_cena = round(float(input("Ievadiet 1 gab. cenu : ")), 2)#formatā ar 2sk aiz komata
    
    #Atlaides var izvelēties. ierakstot konkrētu skaitli no 1-5
    print('\n1-Maxima: 30% atlaide \n2-Elvi: 40%, ja ir karte \n3-Rimi: 20%, bet 50%, ja ir Rimi karte \n4-Mego: 30%, ja pērk 3 un vairāk preces \n5-Top: Katra otrā prece pa brīvu')
    atlaides_veids = input("Izvēlieties, kurā veikalā iepirksieties(Rakstiet ciparu no 1-5) : ")
    
    cena_bez_atlaides = produkta_cena*precu_skaits #iegūst cenu bez atlaides
    pirkuma_cena = cena_bez_atlaides #No pirkuma_cenas rēķinās atlaides

    #sākas atlaižu aprēķināšana
    if atlaides_veids == '1': #Atlaide Maximā
        #pirkuma_cena = pirkuma_cena*0.7
        pirkuma_cena*=0.7 #izmanto salikto reizināšanas operatoru

    elif atlaides_veids == '2': #atlaide Elvi
        card = input("Ievadiet 1, ja ir kl.karte, 0, ja nav ")
        if card == "1":
            pirkuma_cena*=0.6 #atlaide 40%
    
    elif atlaides_veids == "3": #Rimi atlaide
        card = input("Ievadiet 1, ja ir kl.karte, 0, ja nav ")
        if card == "1":
            pirkuma_cena*=0.5
        else:
            pirkuma_cena*=0.8
        
    elif atlaides_veids == '4':
        if precu_skaits >= 3:
            pirkuma_cena*=0.7

    elif atlaides_veids == '5':
        if precu_skaits%2==0:
            pirkuma_cena/=2
        else:
            pirkuma_cena -= produkta_cena    #atņemsim 1 gabala cenu no kopējās cenas
            pirkuma_cena/=2                  
            pirkuma_cena+=produkta_cena
    
    cena_bez_atlaides = round(cena_bez_atlaides, 2)
    pirkuma_cena = round(pirkuma_cena, 2) #Noapaļo rez ar 2 cipariem aiz komata

    summa_bez_atlaides+=cena_bez_atlaides #iegūst summu
    kopsumma+=pirkuma_cena 

    
    ceks+=produkts+'\n'+str(produkta_cena) +'X'+str(precu_skaits)+str(cena_bez_atlaides)+"\nAr atlaidi:\t\t\t" + str(pirkuma_cena)
    stop = input('Viss nopirkts? Jā - 1, nē - 0')

round(summa_bez_atlaides,2 )
round(kopsumma, 2)


ceks+=f"Kopā bez atlaides(EUR):\t{summa_bez_atlaides}\nKopā ar atlaidēm(EUR):\t\t{kopsumma}\n\n"
ceks+=f'Kopā apmaksai(EUR):\t\t{kopsumma}'
print(ceks)

