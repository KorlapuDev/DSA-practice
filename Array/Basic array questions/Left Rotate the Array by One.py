#brutforce method
def left_rotate_one():
    tem_arr = [0] * len(arr1)

    for i in range(1, len(arr1)):
        tem_arr[i - 1] = arr1[i]
    tem_arr[len(arr1) - 1] = arr1[0]
    return tem_arr

# optimaized method 

def left_rotate_one():
    first_element = arr1[0]
    for i in range(1, len(arr1)):
        arr1[i - 1] = arr1[i]
    arr1[len(arr1) - 1] = first_element
    return arr1

arr1 = [1, 2, 3, 4, 5]

result = left_rotate_one()
optimal_result = left_rotate_one()
print(result)
print(optimal_result)
