
tot_terms = int(input("Enter the number of Fibonacci terms to be made: "))


if tot_terms <= 0:
    print("Number of terms must be a positive")
else:
    
    num1, num2 = 0, 1

    
    print("Fibonacci sequence:", num1, num2, end=" ")

    
    for _ in range(tot_terms - 2):
        next_term = num1 + num2
        print(next_term, end=" ")

    
        num1, num2 = num2, next_term



    
    
    

