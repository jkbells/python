# exceptional handing 

def div(num,den):
    return num/float(den)
    
    div (4,3)
    
    div (4,0) # so in this case we use eceptional handling
    
    try:
    print ("div 4 by 3 is: " ), div (4,3)
    print ("div 4 by o is:" ), div (4,0)
    print ("everything is divided successfully")
except:
        print ("do not ask me to divide by 0 please")
        
        
    
