#zadanie 1

print ("To jest program pokazujacy dzielniki liczby, wpisz liczbę: ")

a = int(input())
for i in range(a):
    if a % (i+1) == 0:
        print ("Wprowadzona liczba podzielna jest przez:" + str(i+1))
        
        
#program wyswietla kolejne dzielniki wpisanej przez uzytkownika liczby
        
    