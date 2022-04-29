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
    symbolsList = symbolsList1 + symbolsList2
    includedList = list()
    
    if includeLower:
        includedList = includedList + alphabetLower
    
    if includeUpper:
        includedList = includedList + alphabetUpper
        
    if includeNumbers:
        includedList = includedList + numberList
        
    if includeSymbols:
        includedList = includedList + symbolsList
    
    # Prints
    print(alphabetLower)
    print(alphabetUpper)
    print(numberList)
    print(symbolsList)
    print(includedList)
    
    return includedList

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
    
    includedList = makeIncludedList(includeLower, includeUpper, includeNumbers, includeSymbols)
    
    if includeLower == False and includeUpper == False and includeNumbers == False and includeSymbols == False:
        print("Your Password is: ")
        print("Yes it's blank.")
    else:
        print("yes")

    
    
    # Prints for all inputs & lists
    print("Pass Length: " + str(passLength))
    print("includeLower: " + str(includeLower))
    print("includeUpper: " + str(includeUpper))
    print("includeNumbers: " + str(includeNumbers))
    print("includeSymbols: " + str(includeSymbols))
    print("includedList: " + str(includedList))
    
    
    
    
                        
    

# [2] Ping
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

#open in integrated terminal
#git add PassGen.py
#git commit -m ""