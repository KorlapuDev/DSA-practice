
def checkIfArrisSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True 

arr1 = [1,2,3,4,5]
arr2 = [5,4,6,7,8]

print(checkIfArrisSorted(arr1))  # Output: True
print(checkIfArrisSorted(arr2))  # Output: False