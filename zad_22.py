#zad22
import numpy as np


def mediana(lista):
   lista.sort()
   dlug = len(lista)
   print(dlug)
   print(lista)
   if len(lista) / 2 != 0:
       return lista[int((dlug) / 2)]
   else:
       tymcz = dlug / 2
       return (lista[tymcz - 1] + lista[tymcz]) / 2
    
#By obliczyć medianę,użytkownik wpisuje w konsolę listę liczb z których chce
#otrzymać mediane w formie "x = [y1, y2, ... ,yn] a nastepnie wpisuje mediana(x)