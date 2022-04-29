

def menu():
    print("[1] Password Generator")
    print("[2] Ping")
    print("[0] Option 0")

# def inputChecker()

# [1] Password Generator
def option1():
    answer = str
    passLength = int
    
    answer = str(input("Enter password length: "))

    while answer.isdigit() != True:
        answer = str(input("Invalid. Enter an integer for password length: "))
    
    passLength = int(answer)
    print(passLength)
    
    # includeLower = int(input("Include lowercase? (y/n): "))
    
    # includeUpper = int(input("Include uppercase? (y/n): "))
    
    # includeNumbers = int(input("Include numbers? (y/n): "))
    
    # includeSymbols = int(input("Include symbols? (y/n) "))
    
    
    
    
    

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