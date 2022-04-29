def menu():
    print("[1] Password Generator")
    print("[2] Ping")
    print("[0] Option 0")

# Function to return True/False based on (y/n) inputs
def checkYesNo(answer):
    return answer == "y"

# [1] Password Generator
def option1():
    
    # Password Length
    answer = str(input("Enter password length: "))
    while answer.isdigit() != True:
        answer = str(input("Invalid. Enter an integer for password length: "))
    
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
    answer = str(input("Include numbers? (y/n): "))
    while answer != "y" and answer != "n":
        answer = str(input("Invalid. Enter (y/n): "))
    
    includeNumbers = checkYesNo(answer)
    
    # Include Symbols
    answer = str(input("Include symbols? (y/n): "))
    while answer != "y" and answer != "n":
        answer = str(input("Invalid. Enter (y/n): "))
    
    includeSymbols = checkYesNo(answer)
 
    print(passLength)
    print(includeLower)
    print(includeUpper)
    print(includeNumbers)
    print(includeSymbols)

# [2] Ping
def option2():
    print("Pong.")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        option1()
    elif option == 2:
        option2()
    else:
        print("Invalid Selection.")
        
    print()
    menu()
    option = int(input("Enter your option: "))

print()
print("Exiting program.")

#open in integrated terminal
#git add PassGen.py
#git commit -m ""