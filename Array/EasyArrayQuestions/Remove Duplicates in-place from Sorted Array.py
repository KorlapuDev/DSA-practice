arr1 = [1,1,2,2,2,3,3]
removedArr = [arr1[0]]
for i in range(1, len(arr1)):
    if arr1[i] != arr1[i-1]:
        removedArr.append(arr1[i])

print(removedArr)


