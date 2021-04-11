# file handling 

directory = 'res1'
name = 'jawad.txt'

import os

filename = os.path.join(directory,name)
print (filename)

f= open(filename,'r')  # handle
for line in f:
    print (line.strip())
    
f.close()

# also no needed to close the file

with open(filename,'r') as f:
    for line in f:
        print (line.strip())
        
        # even more concisely

with open(filename,'r') as f:
    print (f.read())  # the whole file
    
    l=[]

with open(filename,'r') as f:
    l=f.read().split('\n')
    
    l
    
    
