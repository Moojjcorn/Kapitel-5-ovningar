while True:
    Time1 = input("\nSkriv in en tid på dygnet i formatet 'TT:MM': ")
    Time2 = input("\nSkriv in en till tid på dygnet som är efter den första, i formatet 'TT:MM': ")

    Time1Split = Time1.split(':')
    Time2Split = Time2.split(':')
    #Omvandla till int för att kunna räckna
    #Veta hur man räcknar med specifikt en del av splitten
    #Jag behöver omvandla allt till minuter
    #Sedan subtrahere dem, den större med den mindre. dvs: Time2 - Time1
    print(Time1Split)
    print(Time2Split)
