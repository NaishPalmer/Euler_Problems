#Problem 2 of Project Euler 
n1 = 0
n2 = 1
nth = n1 + n2
sum_of_even_nths = 0
while nth <= 4000000:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    if nth % 2 == 0:
        sum_of_even_nths += nth
        
        print(sum_of_even_nths)

    
