y = 0
for x in range(0,1000):
    if x % 5 == 0:
        y = x + y
    elif x % 3 == 0:
        y = x + y 
    else:
        pass
    print('x = ' + str(x))
    print(y)

        
