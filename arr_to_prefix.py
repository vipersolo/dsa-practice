arr = [1, 2, 3, 4, 5]

prefix = [0] * len(arr)
prefix[0] = arr[0]
for i in range(1,len(arr)):
    prefix[i] = prefix[i-1]+arr[i]

#range prefix

l=2
r= 4

sum = prefix[r] - prefix[l-1]
print(sum)

#---------------------------------
#if l=0 r= ~ ie (0-1) case wrong soo justgive a condition check
#---------------------------------

# arr = [1, 2, 3, 4, 5]

# prefix = [0]*len(arr)
# prefix[0] = arr[0]

# for i in range(1,len(arr)):
#     prefix[i] = prefix[i-1] + arr[i]

# l = 2
# r = 4

# if l == 0:
#     sum_range = prefix[r]
# else:
#     sum_range = prefix[r] - prefix[l-1]

# print(sum_range)
