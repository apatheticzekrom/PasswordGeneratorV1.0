from random import randint, shuffle

def menu():
    print("[1] Password Generator")
    print("[2] Ping")
    print("[0] Option 0")


# Function to return True/False based on (y/n) inputs
def checkYesNo(answer):
    return answer == "y"


# Function to create list of all possible chars
def makeIncludedList(includeLower, includeUpper, includeNumbers, includeSymbols):
    # Lists
    alphabetLower = list(map(chr, range(97, 123)))
    alphabetUpper = list(map(chr, range(65, 90)))
    numberList = list(map(chr, range(48, 57)))
    symbolsList1 = list(map(chr, range(33, 47)))
    symbolsList2 = list(map(chr, range(58, 64)))
    symbolsList = symbolsList1 + symbolsList2    # symbolsList = [*symbolList1, *symbolList2]
    includedList = list()
    
    # Adds lists needed into includedList
    if includeLower:
        includedList = includedList + alphabetLower
    
    if includeUpper:
        includedList = includedList + alphabetUpper
        
    if includeNumbers:
        includedList = includedList + numberList
        
    if includeSymbols:
        includedList = includedList + symbolsList
    
    return includedList


# Generates password
def generatePassword(passLength, includedList):
    password = list()
    shuffle(includedList)

    for x in range(passLength):
        num = randint(0,len(includedList))
        password.append(includedList[num])
    
    return password


# [1] Password Generator
def option1():
    
    # Password Length
    answer = str(input("Enter password length: "))
    while answer.isdigit() != True:
        answer = str(input("Invalid. Enter an integer: "))
    passLength = int(answer)
    
    # Include Lowercase
    answer = str(input("Include lowercase? (y/n): "))
    while answer != "y" and answer != "n":
        answer = str(input("Invalid. Enter (y/n): "))
    includeLower = checkYesNo(answer)
    
    # Include Uppercase
    answer = str(input("Include uppercase? (y/n): "))
    while answer != "y" and answer != "n":
        answer = str(input("Invalid. Enter (y/n): "))
    includeUpper = checkYesNo(answer)
        
    # Include Numbers
    answer = str(input("Include numbers?   (y/n): "))
    while answer != "y" and answer != "n":
        answer = str(input("Invalid. Enter (y/n): "))
    includeNumbers = checkYesNo(answer)
    
    # Include Symbols
    answer = str(input("Include symbols?   (y/n): "))
    while answer != "y" and answer != "n":
        answer = str(input("Invalid. Enter (y/n): "))
    includeSymbols = checkYesNo(answer)
    
    # Calls makeIncludedList and returns into includedList
    includedList = makeIncludedList(includeLower, includeUpper, includeNumbers, includeSymbols)
    
    # If user says n/n/n/n, then their password contains nothing
    if includeLower == False and includeUpper == False and includeNumbers == False and includeSymbols == False:
        print("Your Password is: ")
        print("Yes it's blank.")
    else:
        password = generatePassword(passLength, includedList)
        print("Your password is: " + str(password))
             
    
# [2] Ping (Added this just cuz) (Gamer Status)
def option2():
    print("Pong.")


menu()
option = str(input("Enter your option: "))

while option != "0":
    if option == "1":
        option1()
    elif option == "2":
        option2()
    else:
        print("Invalid Selection.")
        
    print()
    menu()
    option = str(input("Enter your option: "))

print()
print("Exiting program.")