arr= [1,2,3,4]
count=0
prefix = 0
target = 3
needed = 0
seen = {0:[-1,]}
subarrays= []
for i,element in enumerate(arr):
    prefix+=element

    needed=prefix-target

    if needed in seen:
        for listelement in seen[needed]:
            count+=1
            subarrays.append([listelement+1,i])
    
    if prefix not in seen:
        seen[prefix]=[]

    seen[prefix].append(i)

print(seen)
print(subarrays)