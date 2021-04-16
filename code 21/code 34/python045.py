# String Formatting

x = 24
y = 97

print "x=", x, "and y=", y


# Alternative method: string formatting

print "x=%d and y=%d" % (x, y)   # old method (can also add a second variable)
# Alternatively: 
print "x={} and y={}".format(x, y)   # new method



x = 24.5887676
y = 97



print "x=%f and y=%d" % (x, y)
print "x=%.2f and y=%d" % (x, y)


# Padding

l = [1, 98, 23, 198]
for i in l: 
    print "%4d" % i      # or can use a 0-padding
    
    

for i in l: 
    print "{:03}".format(i)  # also supports 0-padding


s = "Test"
print "[%10s]"%s      # can also do right-padding with a -

# using :n for padding, right padding with a > 
print "={:>10}=".format(s)

# String formatting into variables



s = "Test" 
x = "={:>10}=".format(s)    # can also use the old format here 
print x





