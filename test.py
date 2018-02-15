
#def foo():   function to add only numbers in a list
 #   total = sum(filter(lambda i: isinstance(i, int), l))
  #  print(total)

#foo()

def enterItems ():
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
    total =  sum(int(x[1]) for x in myList) #This adds all the second elements of each tuple in list myList. Instead of sum(...) you can also use sum((...)) or sum([...]). The former uses a generator expression, the latter creates a temporary list (list comprehension).
    print("Your total shopping is: ")
    print(total)



print ("Select a Category")
print ("1: Grocery")
print ("2: Utility Bills")
print ("3: Entertainment")
print ("4: Travel")
print ("5: Car")

choice = input("Enter Choice (1/2/3/4/5) or q to quit :")

if choice == '1':
    print("Welcome To Grocery Section!")
    enterItems()
    #choice = input("Do you want to switch to a different category? Enter Choice (1/2/3/4/5) or q to quit :")

elif choice == '2':
    print("Welcome to the Utility Bills Section!")
    enterItems()

elif choice == '3':
    print("Welcome to the Entertainment Section!")
    enterItems()

elif choice == '4':
    print("Welcome to the Travel Section!")
    enterItems()

elif choice == '5':
    print("Welcome to the Car Section!")
    enterItems()

elif choice == 'q':
    print("End of Program !")
    #print("your total is") create and add a total function using the enteritems function

else:
    print("Invalid Input!")


