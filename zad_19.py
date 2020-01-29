slownik = {"styczen": "31",
          "luty": "28",
          "marzec": "31",
          "kwiecien": "30",
          "maj": "31",
          "czerwiec": "30",
          "lipiec": "31",
          "sierpien": "31",
          "wrzesien": "30",
          "pazdziernik": "31",
          "listopad": "30",
          "grudzien": "31"}

def ilosc_dni(miesiac):
    return slownik[miesiac]

#aby wyswietlić jak dni ma interesujacy uzytkownika miesiac, po zaladowaniu programu wpisuje 
#w konsole slownik["x"] gdzie x to nazwa miesiąca