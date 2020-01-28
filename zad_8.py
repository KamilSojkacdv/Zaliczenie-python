#zadanie 8

while 1: 
    print ("wprowadź ilosc punktów")
    punkty = float(input())
    procenty = (punkty / 40)

    if (procenty<0.39):
        print ("ndst")
    elif (procenty<0.49):
        print ("dop")
    elif (procenty<0.69):
        print ("dst")
    elif (procenty<0.84):
        print ("db")
    elif (procenty<0.99):
        print ("bdb")
    elif (procenty ==1):
        print ("cel")
    print ("Koniec wcisnij n, kolejne oceny wcisnij 2")
    decyzja = input()
    if decyzja == "n":        
        break
    elif decyzja =="2":
        
        
#program oblicza na podstawie % wyniku egzaminu ocenę
        
        