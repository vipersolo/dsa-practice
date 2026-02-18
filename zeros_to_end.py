#-------------------------
#This Swaps 0, order is lost. Wrong answer.
#-------------------------

# arr = [0,1,0,3,12]

# left= 0
# right= len(arr)-1

# while left<right:
#     if arr[left]==0:
#         arr[left],arr[right]=arr[right],arr[left]
#         right-=1
#     left+=1

# print(arr)

#------------------------
#left is 0 , each element checked , non zero swapped. left incremeneted Order preserved.O(1)
#------------------------

arr = [0,1,0,3,12]
left=0

for i in range(len(arr)):
    if arr[i] !=0:
        arr[left],arr[i]=arr[i],arr[left]
        left+=1
print(arr)