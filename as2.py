def menuchoice(userName):
    choice = str.upper(input("\n Tropical Airline Ordering System.\n\n Enter your choice:\n(I)nstrutions\n(O)rder ticket\n(E)xit"))
    while choice !="I" and choice !="O" and choice !="E":
        print("Invalid menu choice.")
        choice = str.upper(input("\n Tropical Airline Ordering System.\n\n Enter your choice:\n(I)nstrutions\n(O)rder ticket\n(E)xit"))
    while choice =="I":
        print("\nThank you for choosing Tropical Airlines for your air travel needs. You will be asked questions regarding what type of ticket you would like to purchase as well as destination information. We also offer 50% discounted fares for children.\n\nTropical Airlines Ticket Ordering System.")
        choice = str.upper(input("\n Tropical Airline Ordering System.\n\n Enter your choice:\n(I)nstrutions\n(O)rder ticket\n(E)xit"))
        while choice != "I" and choice != "O" and choice != "E":
            print("Invalid menu choice.")
            choice = str.upper(input("\n Tropical Airline Ordering System.\n\n Enter your choice:\n(I)nstrutions\n(O)rder ticket\n(E)xit"))
    while choice =="O":
        ticketUser = str.upper(input("\n" + userName + ", is this ticket for:\n(Y)ou \n(S)omeone else\n"))
        if ticketUser =="S":
            user = str(input("\n Please enter the name of the person travelling.\n"))
        elif ticketUser =="Y":
            user = userName
        return user
    if choice =="E":
        print("\n Thank your for visiting Tropical Airlines")
def seat(seatType):
    seatType = str.upper(input("Is this a return trip(R) or One-Way(O)"))
    while seatType!="R" and seatType!="O":
        print("Invalid menu choice")
        seatType = str.upper(input("Is this a return trip(R) or One-Way(O)"))
    return seatType
def getDesR(destR):
    while destR !="C" and destR !="S" and destR !="P":
        print("Invalid menu choice.")
        destR =str.upper(input("\n Please select the destination for your return trip. Fare prices are listed below.\n(C)airns -$400 \n(S)ydney -$575 \n(P)erth -$700"))
    if destR =="C":
        fare = 400
        destName = "Cairns"
    elif destR =="S":
        fare = 575
        destName ="Sydney"
    elif destR =="P":
        fare = 700
        destName ="Perth"
    return  fare, destName
def getDesO(destO):
    while destO !="C" and destO !="S" and destO !="P":
        print("Invalid menu choice.")
        destO =str.upper(input("\n Please select the destination for your return trip. Fare prices are listed below.\n(C)airns -$250 \n(S)ydney - $420 \n(P)erth - $510"))
    if destO =="C":
        fare = 250
        destName ="Cairns"
    elif destO =="S":
        fare = 420
        destName ="Sydney"
    elif destO =="P":
        destName ="Perth"
    return fare, destName
def getTypeofFare(typeofFare):
    while typeofFare!="B" and typeofFare!="E" and typeofFare!="F":
        print("Invalid menu choice.")
        typeofFare =str.upper((input("\n Please choose the type of fare. Fees are displayed below and are in addition to the basic fare.\nPlease note choosing Frugal fare means you will not be offered a seat choice.\n (B)usiness -$275 \n(E)conomy-$25 \n(F)rugal -$0")))
    if typeofFare =="B":
        typeFare = 275
    elif typeofFare =="E":
        typeFare = 25
    elif typeofFare =="F":
        typeFare =0
    return typeFare
def getTypeofSeat(typeofSeat):
    while typeofSeat!="W" and typeofSeat!="A" and typeofSeat!="M":
        print("Invalid menu choice.")
        typeofSeat =str.upper(input("\n Please choose the seat type.  Choosing the middle seat will deduct 25 from the total fare.\n(W)indow -$75 \n(A)isle -$50 \n(M)iddle -$-25"))
    if typeofSeat =="W":
        seatFare = 75
    elif typeofSeat =="A":
        seatFare = 50
    elif typeofSeat =="M":
        seatFare =-25
    return seatFare
def calcTotal(dest, seatChoice, seatType):
    totalPrice = int(dest +seatChoice +seatType)
    return totalPrice
def main():
    userName = str(input("What is your name:"))
    print("Welcome", userName)
    name = menuchoice(userName)
    seatType = seat(type)
    if seatType =="R":
            dest = getDesR(seatType)
    elif seatType =="O":
            dest = getDesO(seatType)
    seatChoice= getTypeofFare(seat)
    if seat =="B" and seat =="E":
        getTypeofSeat(seat)
    else: getTypeofSeat(0)
    userAge =int(input("\nHow old is the person travelling?Travellers under 16 years old will receive a 50% discount for the child fare."))
    if userAge > 16:
        totalFare = calcTotal(dest, seatChoice, seatType)
    else:
        totalFare =calcTotal(dest, seatChoice, seatType)*0.5
    print("Calculating Fare...")
    print("\n\n Ticket for:", name,"\n", dest,"\n", seatType,"\n",seatChoice,"\nAge:",userAge,"\nTotal price:",totalFare)

main()