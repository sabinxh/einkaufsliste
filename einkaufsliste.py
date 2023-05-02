#features: soll solange abfragen bis man keine items hat und dann sollen items geprinted werden in einer liste oder untereinander
from pyautogui import *
from time import sleep

# method to find the search bar location
def click_search_name(name):
    x1, y1 = [500, 200]
    moveTo(x1, y1)
    click()
    typewrite(name, interval=0.2)
    sleep(2)
    press("enter")

# method to find and send message
def click_send_message(msg): 
    x3, y3 = [1155,1000] 
    moveTo(x3, y3) 
    click() 
    sleep(2) 
    typewrite(msg) 
    press("enter")
          
#contact list
kontakte= ["Sascha 🧸", "Alina 🦁"]

print("Was willst du einkaufen?")
einkaufsitem = input("Gebe deinen Einkaufsitem ein: ")
einkaufsliste = []

#while schleife fragt bis kein item hinzugefügt wird
#einkaufsitem hinzufügen in die liste
#liste updaten

while einkaufsitem != "Nein" and einkaufsitem != "nein":
    einkaufsliste.append(einkaufsitem)
    einkaufsitem = input("Willst du noch was hinzufügen? ")

sleep(2)

#iterating through the contact list
for name in kontakte:
    try:
        click_search_name(name)
    except:
        print("Name nicht in Search bar gefunden.")

    try:
        click_send_message(item for item in einkaufsliste)
    except:
        print("Text bar nicht gefunden.")
