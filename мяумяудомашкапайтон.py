lst = [1,2,3,4,5,6,7,8,9]

def find_index(lst):
    if not lst:
        return None

    min_value = lst[0]
    min_index = 0

    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_index = 1

    return min_index
print(find_index(lst))