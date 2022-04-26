def menu():
    print("[1] Option 1")
    print("[2] Option 2")
    print("[0] Option 0")

def option1():
    print("Option 1 selected.")
    
def option2():
    print("Option 2 Selected.")

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