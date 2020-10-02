def intersection(arrays):
    """
    YOUR CODE HERE
    """
    
    
    arr_store = []

    for array in arrays:
        arr_store += array

    cache = {}

    for num in arr_store:
        if num in cache:
            cache[num] += 1
        else:
            cache[num] = 1

    result = []

    for key in cache.keys():
        if cache[key] == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
