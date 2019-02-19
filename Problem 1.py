#Project Euler Problem 1 in Python
y = 0
for x in range(0,1000):
    if x == 999:
       print('The sum of any multiple of 3 or 5 under 1000 is = ' + str(y)) 
    elif x % 5 == 0:
        y = x + y
    elif x % 3 == 0:
        y = x + y

    else:
        pass
