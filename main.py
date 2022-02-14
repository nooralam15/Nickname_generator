#Intiliaze a global value that will fetch the text file and store it in an array
nickNames = list(open('nickname.txt', 'r')) 


#intitialize a function that will display the menu
def menu():
    print("hiiiii")

#initialize a function that will fetch the text data and store it into an array
def dataProcessing(): 
    nickNames.insert(1,"bye")
    print(nickNames[1:3])


#initiliaze a main function that will invoke the other functions 
def main():
    menu()
    dataProcessing()

main()
