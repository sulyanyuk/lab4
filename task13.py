from random import randint

def create2DArray(x,y):
    array = []
    for i in range(0,x):
        array.append([])
        for j in range(0,y):
            array[i].append([])
            array[i][j] = randint(1,9)
    return array



def display2DArray(array):
    for i in range(0,len(array[0])):
        for j in range(0,len(array)):
            print(str(array[j][i]),end=' ')
        print('')

a = 5

x = a
y = a



array = create2DArray(x,y)
display2DArray(array)

print("----------------")

def TASK(array):
    for i in range(0,len(array[0])):
        for j in range(0, len(array)):
            if j < i:
                array[i][j] = '0'

TASK(array)

display2DArray(array)