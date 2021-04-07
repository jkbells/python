# finding the even numbers in a list

nums=[1,2,3,4,5,6]
evens=[]

for i in nums:
    if i%2==0:
        evens.append(i)

print (evens)


# another way to do this

evens=[i for i in nums if i%2==0]
print (evens)


