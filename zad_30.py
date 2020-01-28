#zad 30 

import numpy as np 
import matplotlib.pyplot as plt 
from collections import Counter 
from scipy.stats import kurtosis

def skosnosc(lista):
    avg=np.mean(lista)
    return 1/len(lista)*sum((lista-avg)**3)/(np.std(lista))**3

liczby=np.random.normal(size=1000)

plt.hist(liczby)

print("Srednia wynosi: {}".format(np.mean(liczby))) #wyswietla srednia wygenerowanych liczb
print("Mediana wynosi: {}".format(np.median(liczby))) #wyswietla mediane wygenerowanych liczb
print("Dominanta wynosi: {}".format(Counter(liczby).most_common(1))) #wyswietla dominante wygenerowanych liczb
print("Odchylenie standardowe wynosi: {}".format(np.std(liczby))) #wyswietla odchylenie stand. liczb
print("Wariancja wynosi: {}".format(np.var(liczby))) #wyswietla wariancje wygenerowanych liczb
print("Skosnosc wynosi: {}".format(skosnosc(liczby))) #wyswietla skosnosc wygenerowanych liczb
print("Kurtoza wynosi: {}".format(kurtosis(liczby))) #wyswietla kurtoze wygenerowanych liczb



