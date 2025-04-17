def dota():
    suma = 0
    N = 0
    summation = 0

    while N != 100:
        N = N+1

        if N % 5 == 0:
            print(N)

            summation = summation + N
    print("Result of summation of 5 multiples:", summation)
dota()
