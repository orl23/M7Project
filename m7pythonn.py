import string
from functions import *

def main(): 
    # creates a list of digits 0-9
    passwordNumbers = list(string.digits)
    # creates a list of lowercase and uppercase letters
    passwordAlphabet = list(string.ascii_letters)
    # list of special characters
    passwordSymbols = ["!","@","#","$","%","^","&","*","(",")"] 
    # Initializing a variable named password as an empty list
    password = []
    # Storing the return values from the function askForUserInput as variables
    passwordDesiredLength,passwordNumbersLength,passwordAlphabetLength,passwordSymbolsLength = askForUserInput()
    # Storing the return value from the function getPasswordLength as a variable
    passwordActualLength = getPasswordLength(passwordNumbersLength, passwordAlphabetLength, passwordSymbolsLength)

    checkPasswordLength(passwordDesiredLength, passwordActualLength)
    # line 20 is getting random number line 21 is getting random uppercase or lowercase, and line 22 is getting random symbols.
    # based on user specified value and adding to password list 
    getCharacter(password, passwordNumbersLength, passwordNumbers)
    getCharacter(password, passwordAlphabetLength, passwordAlphabet)
    getCharacter(password, passwordSymbolsLength, passwordSymbols)

   # print("".join(password))
    printToFile(password)

    readFromFile()
    
main()