def main8():
    a = int(input("enter values "))
    b = int(input())

    if a < b:
        temporal = b
        b = a
        a = temporal
    print(temporal, b)
main8()