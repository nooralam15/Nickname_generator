#Intiliaze a global value that will fetch the text file and store it in an array
nickNames = list(open('nickname.txt', 'r'))


#intitialize a function that will display the menu
def menu(firstName, lastName):
  #print the the title of the menu
  print("Main Menu (" + firstName + " " + lastName + ")")

  #initialize variable
  loop = True 

  #create a while loop that will loop through the menu
  while loop:
    userInp = int(input("Enter the number \n 1. Change Name \n 2. Display a Random Nickname \n 3. Display All Nicknames \n 4. Add a Nickname \n 5. Remove a Nickname \n 6. Exit  \n"))

    if userInp == 1:
      askName()

    elif userInp == 2:
      randomName()
    
    elif userInp == 3:
      allName()
    
    elif userInp == 4:
      addName()
    
    elif userInp == 5:
      removeName()
    
    elif userInp == 6:
      print("program closed")
      loop = False
    
    else: 
      print("Invalid Response")


def askName():
  firstName = input("Enter your first name: ")
  lastName = input("Enter your last name: ")
  menu(firstName, lastName)

askName()
