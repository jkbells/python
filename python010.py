# a function that finds its a weekday or not 
# and also in this we can use if statement in the function

def is_weekday(day,month,year):
    # we can import the libaray 
    import datetime
    return datetime.datetime(year=year,month=month,day=day).weekday()

if is_weekday(28,9,2017):
    print ("yes it's a weekday")
else:
        print ("weekend!!")
