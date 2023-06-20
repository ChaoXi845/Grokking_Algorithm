def length(arr):
    i = 0
    if arr == []:
        return i
    else:
        value = arr.pop()
        i += 1
        return i + length(arr)
    
a = [1, 2, 3, 4, 9]
print(length(a))