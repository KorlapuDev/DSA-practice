def max_consucutives(req_arr, max_con_key):
    max_count = 0
    current_count = 0
    for i in range(len(req_arr)):
        if req_arr[i] == max_con_key:
            current_count += 1
        if req_arr[i] != max_con_key:
            if current_count > max_count:
                max_count = current_count
            current_count = 0
        if current_count > max_count:
            max_count = current_count
    return max_count    

prices_arr = [1, 1, 0, 1, 1, 1]

print(max_consucutives(prices_arr, 1))