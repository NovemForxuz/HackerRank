# Can refer to Percentile_Rank.py for testing

dataset = []
n = 5

# Getting data inputs
for index in range(n):
    dataset.append(int(input(f"data {index+1}: ")))

# Getting winzorisation level
winzs_lv = int(input("Winzorisation level: "))


# Defining a function to winzorise dataset
def winzor(data, x):
    min_percentile = x
    max_percentile = 100 - x
    result = []

    # current value = t
    # if more than max --> t-1
    # if less than min --> t+1
    aData = sorted(data)  # sorted data is needed to get the next smallest/largest value

    # loop through each data in the dataset
    for data in dataset:
        # find the Percentile Rank (PR) of the data (t)
        perc = find_percentile_rank(data)

        # If PR is less than min_percentile, find next larger value (t+1)
        if perc < min_percentile:
            # find the Percentile Rank (PR) of the new data (t+1)
            perc = find_percentile_rank(aData[binary_search(aData, data)+1])

            # If new PR is less than min_percentile, append next larger value (t+2) to result
            if perc < min_percentile:
                result.append(aData[binary_search(aData, data) + 2])

            # If new PR is not less than min_percentile, append data (t+1) to result
            else:
                result.append(aData[binary_search(aData, data)+1])

        # If PR is more than max_percentile, find next smaller value
        elif perc > max_percentile:
            # find the Percentile Rank (PR) of the new data
            perc = find_percentile_rank(aData[binary_search(aData, data)-1])

            # If new PR is more than max_percentile, append next smaller value (t-2) to result
            if perc > max_percentile:
                result.append(aData[binary_search(aData, data) - 2])

            # If new PR is not more than max_percentile, append data (t-1) to result
            else:
                result.append(aData[binary_search(aData, data) - 1])

        else:
            result.append(data)

    return result


# Finding the index of value of interest in sorted list (binary search algorithm)
def binary_search(arr, data):
    first = 0
    last = len(arr)-1
    indx = -1
    while (first <= last) and (indx == -1):
        mid = (first+last)//2
        if arr[mid] == data:
            indx = mid
        else:
            if data<arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return indx  # return index of value of interest


# Defining a function to calculate percentile rank
# Wrong use of 'percentile' : re-trying
def find_percentile_rank(score):
    # cumulative frequency is the count of all scores less than or equal to score of interest
    cFreq = cumulative_frequency(score)
    # frequency for the score of interest
    freq = dataset.count(score)

    percentile_rank = (cFreq - (0.5 * freq)) / n * 100

    return percentile_rank


# Defining a function to calculate cumulative frequency
def cumulative_frequency(score):
    cfreq = 0   # initialize
    sData = list(set(dataset))  # distinct values

    # loop through dataset(distinct) & count frequencies based on dataset(input)
    for i in range(len(sData)):
        if sData[i] <= score:
            cfreq += dataset.count(sData[i])
    return cfreq


print(winzor(dataset, winzs_lv))

