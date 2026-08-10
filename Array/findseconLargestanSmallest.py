def second_largest_and_smallest(arr1):
    smallest_ele = arr1[len(arr1)-1]
    second_smallest_ele = arr1[len(arr1)-1]
    second_largest = arr1[len(arr1)-1]
    largest_ele = arr1[len(arr1)-1]
    for i in range(len(arr1)-1):
        if(arr1[i] < smallest_ele):
            smallest_ele = arr1[i]
        elif(arr1[i] > largest_ele):
            largest_ele = arr1[i]
        if(arr1[i] < second_smallest_ele and arr1[i] > smallest_ele):
           second_smallest_ele = arr1[i]
        elif(arr1[i] > second_largest and arr1[i] < largest_ele):
            second_largest = arr1[i]
    
    print("Smallest element is ->", smallest_ele)
    print("Largest element is ->", largest_ele)
    print("Second Smallest element is ->", second_smallest_ele)
    print("Second Largest element is ->", second_largest)


arr1 = [1, 3, 4, 2, 7, 7, 5] 

second_largest_and_smallest(arr1)
