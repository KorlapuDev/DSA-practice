arr1 = [2,8,5,3,9,4,1]

for i in range(len(arr1)):
    swaped = False 
    for j in range(len(arr1) - 1):
        if arr1[j] > arr1[j+1]:
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
            swaped = True
    if not swaped:
        break
print(arr1)