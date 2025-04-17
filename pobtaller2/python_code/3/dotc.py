def dotb():
    suma = 0
    N = 0
    summation = 0
    count = 0

    while N != 300:
        N = N+1

        if N % 2 == 1:
            summation = summation + N
            count += 1
    print("Quantity of values:", count)
    print("Summation is:", summation)

dotb()