"""
code migration from c++ to python
"""
import time

def incrementation(prints, operations):
#to make the operation
    for i in range (1,6):

        for j in range(1, 500):

            for k in range(1, 500):
                sum_cuadrados, hip = operations(i,j,k)
                prints(i,j,k,sum_cuadrados,hip)

def operations(i,j,k):

    hip = i*i #elevatatios of h
    op = j*j #elevation of the oposite side
    ady = k*k

    sum_cuadrados = op + ady
    return sum_cuadrados, hip

def prints(sum_cuadrados, hip, j, k, i):
        if sum_cuadrados == hip: #determinate the pitagórica equivalence
            print("cateto opuesto", j)
            time.sleep(5)
            print("cateto opuesto", k)
            time.sleep(5)
            print("cateto opuesto", i)
            time.sleep(5)

        print("Comprobación", j*j , k*k, hip)
        time.sleep(5)

incrementation(prints, operations)
"numero factorial"