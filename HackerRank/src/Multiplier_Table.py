# Defining a function that takes in 3 parameters: multiplier, start index, end index
def multiplication_table(multiplier, start_idx, end_idx):
    # initializing a list named 'result'
    result = []
    # loop through while index is less or equal to end index
    while start_idx <= end_idx:
        # Appending 'multiplier * start_idx' into list
        result.append(multiplier*start_idx)
        # re-initialize index
        start_idx += 1
    # return result (list)
    return result


# Getting required inputs
in_multiplier = int(input("Multiplier: "))
in_start_ind = int(input("Start index: "))
in_end_ind = int(input("End index: "))

# Calling 'multiplication_table' function and printing result
print(multiplication_table(in_multiplier, in_start_ind, in_end_ind))


