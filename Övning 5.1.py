import datetime
while True:
    dt = datetime.datetime.now()
    pernum = input("Skriv ditt personnummer ÅÅÅÅMMDD: ")
    dtpers = dt.strptime(pernum, '%Y%m%d')

    if (dt.month == dtpers.month and dt.day == dtpers.day):
        print("Grattis på födelsedagen")
    else: 
        print("Du fyller inte år idag")