#Importerar modulen datetime
import datetime

#Skapar en loop som är True
while True:
    #Skapar en variabel "dt" som blir som en shortcut för datetime.datetime.now()
    dt = datetime.datetime.now()

    #Tar en input från användaren och ber om personnummer
    pernum = input("Skriv ditt personnummer ÅÅÅÅMMDD: ")

    #Skapar en ny variabel "dtpers" som har datetime.datetime.now().striptime som splittar ditt personnummer till formatet %Y%m%d
    dtpers = dt.strptime(pernum, '%Y%m%d')

    #En If sats som kollar om dagens månad och dag stämmer med ditt personnumers angivna månad och dag 
    if (dt.month == dtpers.month and dt.day == dtpers.day):

        #Printar vv om if satsen är sann
        print("Grattis på födelsedagen")
    else: 
        #En else sats som printar vv om if satsen är falsk
        print("Du fyller inte år idag")