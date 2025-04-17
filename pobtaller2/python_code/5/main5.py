def main5():
    print("enter radius")
    print("enter height")

    R = float(input())
    H = float(input())
    pi = 3.1416

    vol = pi*R**2*H
    area = (2*pi*R**2) + (2*pi*R*H)

    print("the volume is", vol)
    print("the area is", area)
main5()
