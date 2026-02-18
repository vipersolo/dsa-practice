arr = [1, 2, 3, 2, 1]
target = 5

prefix_sum = 0
count = 0

# dictionary to store prefix sum frequencies
seen = {0: 1}

for num in arr:
    # update running prefix sum
    prefix_sum += num
    
    # check if needed prefix exists
    needed = prefix_sum - target
    
    if needed in seen:
        count += seen[needed]
    
    # store/update current prefix sum frequency
    if prefix_sum in seen:
        seen[prefix_sum] += 1
    else:
        seen[prefix_sum] = 1

print("Number of subarrays with sum =", target, "is:", count)


#--------------------------------
#for subarray finding not count ->(for loop due to value of dict may becomes list on array like[0,0,0,0] , seperate starting points are needed)
#--------------------------------

arr = [1, 2, 3, 2, 1]
target = 5

prefix_sum = 0

# dictionary stores: prefix_sum → list of indexes where it occurred
seen = {0: [-1]}   # -1 handles subarrays starting at index 0

result = []

for i, num in enumerate(arr):
    prefix_sum += num
    
    needed = prefix_sum - target
    
    # if needed prefix exists, subarray(s) found
    if needed in seen:
        for start_index in seen[needed]:
            result.append((start_index + 1, i))
    
    # store current index in dictionary
    if prefix_sum not in seen:
        seen[prefix_sum] = []
    
    seen[prefix_sum].append(i)

# print indexes
print("Subarray indexes:", result)

# print actual subarrays
print("Subarrays:")
for start, end in result:
    print(arr[start:end+1])