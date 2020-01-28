#zad 29

def regresja_liniowa(x, y):
    kw_x = 0
    for i in x:
        kw_x += i**2
        
    a = (len(x) * sum(x) * sum(y)) - (sum(x) * sum(y)) / (len(x) * kw_x) - (sum(x)** 2)
    b = (len(x) * kw_x * sum(y)) - (sum(x) - sum(y)) / (len(x) * kw_x) - (sum(x) ** 2)
    return a, b

#by obliczyc regresje liniowa, uzytkownik po uruchomieniu kodu, musi wpisac w konsoli 2 listy 
#rownej dlugosci w formie "x = (...)", "y = (...)" a nastepnie wpisac "regresja_liniowa(x, y)