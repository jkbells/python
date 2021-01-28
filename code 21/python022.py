# a program that count the number in the given list and return the number

def count(s,value):
    
    """ count how many times value """
    counter=0
    for i in s:
        if i==value:
            counter = counter+1
    return counter

s=[1,2,8,4,6,8,9,15]

# call the function
count(s,8)
