#zadanie 13

#algorytm obliczajacy dwumian newtona


def Newton(n, k):    
    if k == 0 or k == n:
        return 1
    else:
        return (n-1, k-1) + (n-1, k)
    
#W celu skorzystania z dwumiannu Newtona, uzytkownik uruchamia skrypt, nastepnie wpisuje w konsoli "Newton x, y" gdzie x, y to liczby.