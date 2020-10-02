def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    #
    #weight as key
    #index as value
    weights_dict = {}


    for indx, weight in enumerate(weights):
        weights_dict[weight] = indx
        print(weights_dict)

        if (limit-weight) in weights_dict:
            print("yep")
            if indx == weights_dict[limit-weight]:
                return [indx+1, weights_dict[limit-weight]]
            else:
                return [indx, weights_dict[limit-weight]]
        else:
            print("nope")
            pass

    
    return None
    

final= get_indices_of_item_weights([4,6,10,15,16], length= 5, limit=21)

print(final)

final = get_indices_of_item_weights([4,4], 2, 8)

print(final)