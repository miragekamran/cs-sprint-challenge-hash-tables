def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Create a dictionary to cache the numbers
    cache = dict()
    # Create an array to keep the results
    result = []

    # Loop through the arrays array
    for array in arrays:
        # and now loop through each number in the arrays
        for num in array:
            # see if the number is in the dictionary
            # then increase it by 1 if not
            # return itself
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1

    # Loop through the keys in the dictionary
    # and see if the keys are maching in the arrays
    # they add them into the result array
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
