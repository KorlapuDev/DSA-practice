arr1 = [2,8,5,3,9,4,1]

for i in range(len(arr1)):
    minIndxEle = i
    for j in range(i+1, len(arr1)):
        if arr1[minIndxEle] > arr1[j]:
            minIndxEle = j
    arr1[i], arr1[minIndxEle] = arr1[minIndxEle], arr1[i]

print(arr1)