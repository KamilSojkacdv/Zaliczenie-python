#z20

slownik = {"styczen": "January",
          "luty": "February",
          "marzec": "March",
          "kwiecien": "April",
          "maj": "May",
          "czerwiec": "June",
          "lipiec": "July",
          "sierpien": "August",
          "wrzesien": "September",
          "pazdziernik": "October",
          "listopad": "November",
          "grudzien": "December"}

def tlumacz(miesiac):
    return slownik[miesiac]

#aby wyswietlić jak brzmi interesujacy uzytkownika miesiac, po zaladowaniu programu wpisuje 
#w konsole slownik["x"] gdzie x to nazwa miesiąca