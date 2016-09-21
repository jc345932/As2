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
        ticketUser = str.upper("\n" + userName + ", ticket for:\n(Y)ou \n(S)omeone else\n")
        if ticketUser =="S":
            user = str(input("\n Please enter the name of the person travelling.\n"))
        elif ticketUser =="Y":
            user = userName
        return user
    if choice =="E":
        print("\n Thank your for visiting Tropical Airlines")
