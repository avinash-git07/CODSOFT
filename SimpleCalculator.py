#simple calculator
def   SimpleCalculator():

    Num1 = int(input("Enter the first number: "))
    Num2 = int(input("Enter the second number: "))


    print("\nSelect operation:")
    print("1.Addition +")
    print("2.Subtraction -")
    print("3.Multiplication *")
    print("4.Division /")

    choice = input("\nEnter  any choice : ")

    if choice == '1':
        print(f"\nResult: {Num1} + {Num2} = {Num1 + Num2}")
    elif choice == '2':
        print(f"\nResult: {Num1} - {Num2} = {Num1 - Num2}")
    elif choice == '3':
        print(f"\nResult: {Num1} * {Num2} = {Num1 * Num2}")
    elif choice == '4':

        if Num2 != 0:
            print(f"\nResult: {Num1} / {Num2} = {Num1 / Num2}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\n Please choose  a valid choice.")


SimpleCalculator()
