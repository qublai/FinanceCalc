class Shoptest:


    def enterItems(self):
        numItems = input("How many items do you want to enter? ")
        myTup = ()  # tuple
        myList = []  # list

        for x in range(int(numItems)):  # the loop will run the number of times entered by the user
            itemName = input("Enter item name: ")
            itemPrice = input("Enter item price: ")
            myTup = (itemName, itemPrice)  # item price and item name entered
            myList.append(myTup)

        myList.sort()

        for x in range(len(myList)): print(myList[x][0] + " = " + myList[x][1])
        total = sum(int(x[1]) for x in myList)  # This adds all the second elements of each tuple in list myList. Instead of sum(...) you can also use sum((...)) or sum([...]). The former uses a generator expression, the latter creates a temporary list (list comprehension).
        print("Your total shopping is: ")
        print(total)