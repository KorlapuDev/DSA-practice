arr1 = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
arrNums = []
arrZeros = []

for i in range(len(arr1)):
    if arr1[i] == 0:
        arrZeros.append(0)
    else:
        arrNums.append(arr1[i])

print(arrNums + arrZeros)