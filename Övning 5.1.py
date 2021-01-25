import datetime
dt = datetime.datetime.now()

mån = dt.month
dag = dt.day
while True:
    personnummer = input("Ange ditt personnummer ÅÅÅÅMMDD: ")
    pn_mån = personnummer[4:6]
    pn_dag = personnummer[6:8]