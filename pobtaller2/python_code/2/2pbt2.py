def compare():
    print("enter values")
    value1 = int(input())
    value2 = int(input())
    value3 = int(input())

    while value1 == value2 or value2 == value3 or value1 == value3:
        print("Values should be different")
        return compare()

    if value1 > value2 and value1 > value3:
        print(value1," is higher")
    else:
        if value2 > value1 and value2 > value3:
            print(value2," is higher")

        else: print(value3," is higher")
compare()