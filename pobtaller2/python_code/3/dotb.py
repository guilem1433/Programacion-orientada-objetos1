def dotb():
    suma = 0
    N = 0
    summation = 0

    while N != 100:
        N = N+1

        if N % 2 == 0:
            print(N)

            summation = summation + N
    print("the summation is:", summation)
dotb()