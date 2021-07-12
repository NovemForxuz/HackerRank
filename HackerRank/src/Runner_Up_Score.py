# Print the runner up score

n = int(input())    # 1st input is 'n' number of scores
arr = map(int, input().split())     # 2nd input is the arr of scores

# Convert to list for list function,
# Apply set function for distinct values
li = list(set(arr))
print(li)

# Sort the list in ascending order
li.sort()

# print the 2nd larger score
print(li[-2])
