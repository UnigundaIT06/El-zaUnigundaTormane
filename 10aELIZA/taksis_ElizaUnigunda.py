
pasazieri = input("Labdien! Cik pasažieri būs taksī braukšanas brīdī? (Līdz 3/ Vairāk par 3) > ")
if pasazieri == "Vairāk par 3":
    print('Atvainojos, bet jūs nevarat saņemt šī takša pakalpojumu dēļ pasažieru skaita. ')
    exit()
elif pasazieri == "Līdz 3":
    laiks = int(input("Lūdzdu, ievadat attiecīgo pulksteņa laiku. > "))
    if laiks >= 21 and laiks <= 24 or laiks >= 1 and laiks <= 6: #Tiek veikta laika norādīšana
        print("Jūsu norādītais laiks sakrīt ar nakts tarifu, tas nozīmē, ka 1km = 0,77 euro. ")
    elif laiks >= 7 and laiks <= 20: #Laiku norādu ar lielāks par, vienāds, mazāks par
        print("Jūsu norādītais laiks sakrīt ar dienas tarifu, tas nozīmē, ka 1km = 0,37 euro.")
    noligsana = input('Vai stacijas stāvvietā ir taksis attiecīgajai firmai? (Nav/Ir) > ')
    if noligsana == "Ir": 
        print("Jums būs jāmaksā 2 euro par nolīgšanu.")   
    elif noligsana == "Nav":            
            print("Jums būs jāmaksā nolīgšana 2 euro un izsaukšana 2,50 euro.")
    else: 
         print("Ievadat pareizu atbildi! ")
         exit() #Beidz darbību, ja kaut kas notiek nepareizi
    gaidisana = int(input("Jums ir iespēja ievadīt gaidīšanas laiku, ja ir jāpiestāj veikalā u.t.t. Ja nav nepieciešams ievadat (0) > "))
    if gaidisana > 0: # gaidīšanas ievade pārveidota par skaitli, kas parādās izdrukā
         print("Par katru", gaidisana, "minūtēm/minūti pienāk klāt 0,15 euro!")
    elif gaidisana == 0:
         print()
    attalums = int(input("Ievadiet nepieciešamo attālumu (km), kādu būs jāveic šoferim. > "))
    if attalums == attalums: #Attāluma ievade un izvade
         print("Šoferim no punkta A uz punktu B būs jābrauc: ", attalums, "km.")
    mDzivnieks = input("Vai brauciena laikā jums kompāniju sastādīs arī mājdzīvnieks? (J/N) >")
    if mDzivnieks == "J":
         print("Šoferis būs ļoti priecīgs un varbūt iedos jums 5 procentu atlaidi! :)")
    elif mDzivnieks == "N": 
         print("Šoferis būs skumīgāks (Uzgriezīs skaļāk mūziku), taču neko neteiks un jūs nesaņemsiet atlaidi.")
         print("") #Lai uztaisītu atlaidi man būtu nepieciešams - kopsumma : 100*5
    ceks = input("Aprēķināsim jums beigu aprēķinus (SPIEŽAT ENTER) > ") #Tiek lūgts lietotājam turpināt darbību, spiežot ENTER, lai izdrukātu beigu aprēķinus


izsauksana = 2.50
noligsana2 = 2
if noligsana == 'Ir':
     print("Samaksa tikai par nolīgšanu> ", noligsana2, "euro") #Summas izvade, ja taksis ir stāvietā. 
elif noligsana == 'Nav':
     print("Jūsu kopēja izmaksa par nolīgšanu un izsaukšanu >", izsauksana+noligsana2, "euro") #Summas saskaitīšana, ja taksis nav stāvvietā

gaidisana2 = 0.15
if gaidisana == 0:
     print("Nav jāmaksā par gaidīšanu")
elif gaidisana > 0:
     print("Jāmaksā par gaidīšanas minūtēm > ", round(gaidisana*gaidisana), "euro") #Ar round noapaļoju rezultātu, ko iegūstu sareizinot skaitļus

naktsTarifs = 0.77
dienasTarifs = 0.37

if laiks >= 7 and laiks <= 20:
     print("Jums jāmaksā par nobrauktajiem KM dienas tarifā > ", dienasTarifs*attalums)
elif laiks >= 21 and laiks <= 24 or laiks >= 1 and laiks <= 6:
     print("Jums jāmaksā par nobrauktajiem KM nakts tarifā > ", round(naktsTarifs*attalums))


        

        

    
            
    