# file casestudy 
# and working with file data

directory = "res"
name = "datafile.csv"

import os

csv_filename = os.path.join(directory,"datafile.csv")
print (csv_filename)

with open(csv_filename,'r') as f:
    for line in f:
        print (line.strip().split(','))  # lets save them in a list
        
        rows = []
with open(csv_filename,'r') as f:
    for line in f:
        print (line.strip().split(','))
    rows.append (line.strip().split(','))
    
    
    rows
    
    for r in rows[1:]:
    for i in range(2,6):
        r[i] = float (r[i])
        
        rows
        
        for r in rows:
    print [str(c) for c in r]
    
    rows
    
    out_rows=[]
for r in rows:
    r = [str(c) for c in r]
    out_rows.append(r)
    
    out_rows
    
    for r in out_rows:
    out_line = ','.join(r)  # and then save this to a file
    
    print (out_line)
    
    csv_filename_out = os.path.join (directory,"datafile_out.csv")
    
    with open(csv_filename_out,'w') as f:
    for r in out_rows:
        out_line=','.join(r)
        f.write(out_line + "\n")
        
        
