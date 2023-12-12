gads = int(input("Ievadi gadu: ")) #Prasa lietotājam ievadīt savu vēlamo gadu. 

if ((gads % 4 == 0 and gads % 100 != 0) or (gads % 400 == 0)): #Ja gads dalās ar 4, bet nedalās ar 100, tad tas ir garais gads.
        print(f"{gads} ir garais gads")
else:
        print(f"{gads} Ir īsais gads") #Ja gads dalās gan ar 4, gan ar 100, gan ar 400, tad tas ir īsais gads. 