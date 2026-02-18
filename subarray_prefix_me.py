arr= [0,0,0]

seen = {0:1}

target = 0
count=0
prefix = 0

for i,element in enumerate(arr):
    prefix+=element

    needed = prefix - target

    if needed in seen:
        count+=seen[needed]


    seen[prefix]=seen.get(prefix,0)+1

print(count)
print(seen)

