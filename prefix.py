
# prefix= [2,6,12,20] #this is normal array but prefix model. ie prefix working.

# l=1
# r=3

# sum = prefix[r] - prefix[l-1]

# print(sum)

# arr=[2,4,6,8]

# prefix = [0]*len(arr)
# prefix[0] = arr[0]

# for i in range(1,len(arr)):
#     prefix[i] = prefix[i-1] + arr[i]

# print(prefix)


arr = [3, 1, 4, 2, 5]

prefix = [0]* len(arr)
prefix[0] = arr[0]

for i in range(1,len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)
