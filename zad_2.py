#zadanie 2


def CnaF(temp):
    return (temp*9/5)+32

def FnaC(temp):
    return (temp-32)*(5/9)


print ("Zamiana stopni C na F, oraz F na C")
print ("C -> F wprowadz 1, f -> c (wprowadź 2)")
decyzja = int(input())
if(decyzja == 1):
    print ("wprowadz temperature")
    temp = float(input())
    wynik = CnaF(temp)
    print("Temperatura to: ")
    print(wynik)
    print("Stopni Fahrenheita")
if(decyzja == 2):
    print ("wprowadz temperature")
    temp = float(input())
    wynik2 = FnaC(temp)
    print("Temperatura to: ")
    print (wynik2)
    print ("Stopni Celcjusza")
   
#program przelicza stopnie F na C, oraz odwrotnie.