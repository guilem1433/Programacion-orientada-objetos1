def dotb():
    while True:
        n = int(input("Enter quantity of values: "))

        if n == "0":
            print("finalization")
            break

        c50_70 = 0
        c_over_80 = 0
        c_less_30 = 0

        print(f"enter {n} values")
        for _ in range(n):
            value = int(input())

            if 50 <= value <= 75:
                c50_70 += 1
            elif value > 80:
                c_over_80 += 1
            elif value < 30:
                c_less_30 += 1

        print(f"numbers (50-75):{c50_70}")
        print(f"numbers over 80:{c_over_80}")
        print(f"numbers under 30:{c_less_30}")
        print("press 0 to finish:")
dotb()
