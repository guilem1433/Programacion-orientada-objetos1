
def comparison():
    print("Enter values: ")

    value1= input()
    value2= input()

    while value1 == value2:
        print("values should be different")
        return comparison()

    if value1 > value2:
        print(f"{value1} is higher")

    else:
        print(f"{value2} is higher")

comparison()