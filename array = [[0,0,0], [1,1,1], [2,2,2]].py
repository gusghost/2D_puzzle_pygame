array = [[0,0,0], 
        [1,1,1], 
        [2,2,2], 
        [4,4,4]]

gridsizex = len(array[0])
gridsizey = len(array)
location = [y, x]
for x in range(gridsizex):
    for y in range(gridsizey):
        a = array[y][x]
        print(array[y][x])