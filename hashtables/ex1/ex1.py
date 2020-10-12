def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create empty dictionary
    storage = dict()


    # loop over the length
    for i in range(length):
        current_weight = weights[i]
        total = (limit - current_weight)

        # if total is in the dictionary,
        # return a tuple of the current index and total index
        # otherwise set the current wieght key to the current index
        if total in storage:
            total_index = storage[total]

            return (i, total_index)
        else:
            storage[current_weight] = i

    # return none if the pair doesn't exist for the given inputs
    return None

print(get_indices_of_item_weights([4, 6, 10, 15, 16, 2], 6, 12))

