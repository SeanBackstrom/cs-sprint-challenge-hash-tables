def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    store = {}
    result = []

    for num in a:
        store[num] = -num

    for num in a:
        if -num in store:
            if num > 0:
                result.append(num)


    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
