#Intiliaze a global value that will store the nickname array
global nickNames 


#intitialize a function that will display the menu
def menu():
    print("hiiiii")

#initialize a function that will fetch the text data and store it into an array
def dataProcessing(): 
    fetch = open('nickname.txt', 'r')
    nickNames = list(fetch)
    print(nickNames[1])


#initiliaze a main function that will invoke the other functions 
def main():
    menu()
    dataProcessing()

main()
