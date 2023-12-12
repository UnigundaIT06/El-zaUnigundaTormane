Pdaudzums = int(input("Sveiki! \nCik daudz preces jūs esat izvēlējušies? >"))
if Pdaudzums < 0:
    print("Atvainojiet, jums ir jāievada derīgs preču skaitlis! ")
elif Pdaudzums > 0:
    print("Esat izvēlējušies", Pdaudzums, "preces.")
    preces = ['Saldējums', 'vīns', 'maize', 'siera maizīte', 'āboli']
    Pnosaukums = input("Preču nosaukumi > ")
    if Pnosaukums == Pnosaukums:
        print("Izvēlējāties šīs preces > ", Pnosaukums)
        Pcenas = int(float(input('Ievadat šo preču kopējo cenu > ')))
        if Pcenas == Pcenas:
       
           saraksts =input("Vai ir nopirkts viss, kas sarakstā? (J/N) >  ")
        if saraksts == "N": 
            print("Sākam no gala! ")
            exit
        elif saraksts == "J":
            print('Izstrādāsim čeku > ')
        
        veikals = input("Kurā veikalā iepirksieties? Rimi, Maxima, Lidl, Lats, Top (R/M/L/LA/T)")
        if veikals == "R":
            print("Jūsu atlaide būs 30% ")
            print("Tagad jāmaksā > ", (Pcenas*30)//100, "Euro")
        elif veikals == "M":
            print('Katra otrā prece pa brīvu. ', Pcenas//2, "Euro")
            print('')
        elif veikals == "L":
            karte = input("Vai jums ir karte? (j/n)")
            if karte == "j": 
                print("Jūsu atlaide tad būs 40%")
                print("Tagad jāmaksā > ", (Pcenas*40)//100, "Euro")
        elif veikals == "LA":
            print("Ja pirksiet 3 un vairāk preces, atlaide ir 30%")
            if Pdaudzums > 3:
                print("Jums pienākas atlaide 30%", (Pcenas*30)//100, "Euro")
        elif veikals == "T":
            print("Jūsu atlaide būs 20%,", ((Pcenas*20)//100))
            karte = input("Vai jums ir karte? (j/n)")
            if karte == "j": 
                print("Pienākas 50% ",(Pcenas*50)//100, "Euro" )

                print("Vai beidzot esam programmas galā? > ")
                end = input("Esam? (j/n)")
                if end == "j":
                    print("Jauki")
                elif end == "n":
                    print("Dodamies atpakaļ uz veikalu? ")

            
        