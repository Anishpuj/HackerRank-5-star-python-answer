def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:            #Here we are checking if the year is normal year
        leap = True
        if year%100 == 0:        #Here we are checking if the year is a century year      
            if year%400 == 0:
                leap = True
            else:
                leap = False
        
                
    

                
    

    return leap


year = int(input())
print(is_leap(year))
