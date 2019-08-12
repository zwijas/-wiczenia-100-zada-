'''Uzyskać prgram, który z kilku list wskaże takie, których wszystkie elementy zawierają się w innej wskazanej liście.
ogólniej - program, który z podanych przepisów wybierze te, na które użytkownik ma składniki'''
import os

#lista składników do potraw
pomidorowa = ["pomiory", "marchewka", "makaron"]
schabowe = ["schab", "panierka", "ziemniaki", "surówka"]
mielone = ["mięso mielone", "panierka", "ziemniaki"]

#pobranie listy produktów, które są w domu:
fridge = []
wskaznik = 1
while wskaznik == 1:
    if len(fridge) == 0:
        print("Wpisz pierwszy produkt z którego chcesz ugortować obiad")
    else:
        print ("Zawartość lodówki:")
        print (fridge)
        print("Wpisz kolejny produkt i wciśnij >enter< lub wpisz >koniec< aby wyszukać przepis")
    produkt = input ()
    produkt = produkt.upper()
    if len(produkt) == 0:
        print ("Ziomku, nic nie wpisałeś, spróbuj jeszcze raz")
        input()
    elif produkt == "koniec":
        if len(fridge) == 0:
            print ("Ziomku, nie dodałeś żadnego produktu, spróbuj jeszcze raz")
            input()
        else:
            wskaznik = 0
    else:
        fridge.append(produkt)
    os.system("cls")
