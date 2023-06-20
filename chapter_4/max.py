def max_in_list(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        first = arr[0]
        rest = arr[1:]
        max_in_rest = max_in_list(rest)
        if first > max_in_rest:
            return first
        else:
            return max_in_rest

a = [2, 5, 10, 8, 4]
print(max_in_list(a))  
