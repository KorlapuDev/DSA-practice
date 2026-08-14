def rotateArrByKelement(arr, k, direction):
    tempArr = []
    eleRotate = []
    if(direction=="right"):
        for i in range(len(arr)):
            if(i > len(arr) - k - 1):
                eleRotate.append(arr[i])
            else:
                tempArr.append(arr[i])
        return eleRotate + tempArr
    
    if(direction=="left"):
        for i in range(len(arr)):
            if(i < k):
                eleRotate.append(arr[i])
            else:
                tempArr.append(arr[i])
        return tempArr + eleRotate




arr1 = [1, 2, 3, 4, 5, 6, 7]

print(rotateArrByKelement(arr1, 2, "right"))