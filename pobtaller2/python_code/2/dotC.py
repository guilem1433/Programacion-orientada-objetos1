def lower2():
    print("enter values")
    value1 = int(input())
    value2 = int(input())
    value3 = int(input())

    while value1 == value2 or value2 == value3 or value1 == value3:
        print("Values should be different")
        return lower2()

    if value1 < value2 and value1 < value3:
        print(value1," is lower")
    else:
        if value2 < value1 and value2 < value3:
            print(value2,"is lower")

        else: print(value3,"is lower")
lower2()