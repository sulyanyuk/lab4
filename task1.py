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
                array[j][i] = "00" + str(array[j][i])
            if len(str(array[j][i])) == 2:
                array[j][i] = "0" + str(array[j][i])
            print(str(array[j][i]),end=' ')
        print('')

x = 5
y = 7

array = create2DArray(x,y)

from random import *
seed("test")
for i in range(0,x):
    for j in range(0,y):
        array[i][j] = randint(1,99)

display2DArray(array)

for j in range(0,y):
    maxInRow = array[0][j]
    maxIndex = 0
    for i in range(0,x):
        if array[i][j] > maxInRow:
            maxInRow = array[i][j]
            maxIndex = i

    if maxIndex == 0:
        array[1][j] = str(int(array[1][j]) * 2)

    if maxIndex == (x-1):
        array[x-2][j] = str(int(array[x-2][j]) * 2)

    if 0 < maxIndex < (x-1):
        if array[maxIndex-1][j] > array[maxIndex+1][j]:
            array[maxIndex+1][j] = str(int(array[maxIndex+1][j]) * 2)
        else:
            array[maxIndex - 1][j] = str(int(array[maxIndex - 1][j]) * 2)

print("------------------")

display2DArray(array)
