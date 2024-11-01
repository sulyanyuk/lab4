def factroial(n):
    n_factorial = 1
    for i in range(1,n+1):
        n_factorial = n_factorial * i
    return n_factorial

def create2DArray(x,y):
    array = []
    for i in range(0,x):
        array.append([])
        for j in range(0,y):
            array[i].append([])
            array[i][j] = '00'
    return array



def display2DArray(array):
    for i in range(0,len(array[0])):
        for j in range(0,len(array)):
            if len(str(array[j][i])) == 1:
                array[j][i] = " " + str(array[j][i])
            print(str(array[j][i]),end=' ')
        print('')

x = 5
y = 7

array = create2DArray(x,y)

from random import *
seed("test34342") ######################### <----- array fill rand seed ##############################
for i in range(0,x):
    for j in range(0,y):
        array[i][j] = randint(-9,9)

display2DArray(array)

negatives = []
for j in range(0,len(array)):
    countedNegs = 0
    for i in range(0,len(array[j])):
        if float(array[j][i]) < 0:
            countedNegs += 1
    negatives.append(countedNegs)

print(negatives)

print("-----------------------------")

i = 0
while True:
    noSwap = True
    for j in range(0,len(negatives)-1):
        if negatives[j] > negatives[j+1]:
            negatives[j],negatives[j+1] = negatives[j+1],negatives[j]
            array[j],array[j+1] = array[j+1],array[j]
            noSwap = False
    i += 1
    if noSwap:
        break

display2DArray(array)
print(negatives)