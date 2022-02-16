#import library
import random
import sys

#Intiliaze a global value that will fetch the text file and store it in an array
nickNames = list(open("nickname.txt", 'r+'))


#Initialize an array that will remove the new lines in the array
def fixArray():
    for x, n in enumerate(nickNames):
        nickNames[x] = n.strip()
fixArray()


#initiliaze a function that displays a random nickName
def randomName(first, second):
    randInt = random.randint(0, len(nickNames))
    print(first + " the " + nickNames[randInt] + " " + second)


#initliaze a function that displays all the nicknames
def allName(first, second):
    #loop through the whole array using for
    for i in range(len(nickNames)):
        print(first + " the " + nickNames[i] + " " + second)


#initiliaze a function that will add a nickname to the array
def addName():
    userInput = input("Enter a nickname: ").lower()
    nickNames.append(userInput)
    print("Nickname has been added")


#initialize a function that will search for a nickname and remove it
def removeName():
    #initialize variables
    userInput = input("Enter a nickname: ").lower()
    #check the array for the name
    if userInput in nickNames:
        nickNames.remove(userInput)
        print("Found and removed")
    else:
        print("Not found")


#intitialize a function that will display the menu
def menu(firstName, lastName):
    #initialize variable
    loop = True
    #create a while loop that will loop through the menu
    while loop:
        #print the the title of the menu
        print("Main Menu (" + firstName + " " + lastName + ")")
        userInp = int(input("Enter the number \n 1. Change Name \n 2. Display a Random Nickname \n 3. Display All Nicknames \n 4. Add a Nickname \n 5. Remove a Nickname \n 6. Exit  \n"
            ))
        
        if userInp == 1:
            askName()

        elif userInp == 2:
            randomName(firstName, lastName)

        elif userInp == 3:
            allName(firstName, lastName)

        elif userInp == 4:
            addName()

        elif userInp == 5:
            removeName()

        elif userInp == 6:
            print("Program closed")
            sys.exit()

        else:
            print("Invalid Response")


#initiliaze a function that will ask for the names
def askName():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    menu(firstName, lastName)
askName()
