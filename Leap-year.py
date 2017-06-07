print ("This function(is_year_leap(year)) specifies a leap year")
def is_year_leap (y):
    if y%400==0:
        print(y," is leap year")
    elif y%4==0 and y%100!=0:
        print(y," is leap year")
    else:
        print(y," is common year")
        
