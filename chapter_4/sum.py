def sum(arr):
    total = 0
    if len(arr) == 0:
        return total
    elif len(arr) > 0:
        value = arr.pop()
        return value + sum(arr)
    
a = [2, 4, 6]
print(sum(a)) 