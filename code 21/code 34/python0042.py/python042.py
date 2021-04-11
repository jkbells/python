# writing the file 

out_name="dummy_out.txt"

out_filename=os.path.join(directory,out_name)
print (out_filename)

with open(out_filename,'w') as f:
    f.write("three ... ")
    
    
