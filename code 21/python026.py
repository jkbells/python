# a program that finds the same pairs in a given list

pairs= [[1,2],[2,2],[2,3],[4,4]]

same_count=0
for x,y in pairs:
    if x==y:
        same_count+=1
print (same_count)


