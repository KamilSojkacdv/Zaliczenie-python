#Zadanie 23
from collections import Counter


def dominanta(x):
    c = Counter(x)
    return c.most_common(1)[0][0]

#By obliczyć dominante,użytkownik wpisuje w konsolę listę liczb z których chce
#otrzymać dominante w formie "x = [y1, y2, ... ,yn] a nastepnie wpisuje dominanta(x)