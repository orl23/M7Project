import random

def getCharacter(password, length, list ):
    for index in range(length):
        password.append(random.choice(list))
# asking user input for length of password
def askForUserInput():
    passwordDesiredLength = int (input("enter password length as a number: "))
    passwordNumbersLength = int (input("enter how many numbers you want: "))
    passwordAlphabetLength = int (input("enter how many letters you want: "))
    passwordSymbolsLength = int (input("enter how many symbols you want: "))
# sending the function result back to caller
    return passwordDesiredLength,passwordNumbersLength,passwordAlphabetLength,passwordSymbolsLength

def getPasswordLength(passwordNumbersLength, passwordAlphabetLength, passwordSymbolsLength): 
    return passwordNumbersLength + passwordAlphabetLength + passwordSymbolsLength

def checkPasswordLength(passwordDesiredLength, passwordActualLength):
     # checking if user entered password length is equal to the length of the character choices they entered
    if(passwordDesiredLength > passwordActualLength):
        print("Password desired is longer than the actual password from given values")
    elif (passwordDesiredLength < passwordActualLength):
        print("Password desired is shorter than the actual password from given values")

def printToFile(password):
    f = open("password.txt", "a")
    f.write("".join(password))
    f.write("\n")
    f.close()

def readFromFile():
    f = open("password.txt", "r")
    print(f.read())
    f.close()

   