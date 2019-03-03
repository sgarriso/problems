
##Have the function Division(num1,num2)
##take both parameters being passed and return the Greatest Common Factor.
##That is, return the greatest number that evenly goes into both numbers with no remainder.
##For example: 12 and 16 both are divisible by 1, 2, and 4 so the output should be 4. The range for both parameters will be from 1 to 10^3. 
##
##Use the Parameter Testing feature in the box below to test your code with different arguments.
def Division(num1,num2): 
    a_factors = primeFactors(num1)
    b_factors = primeFactors(num2)
    a_factors = list(set(a_factors))
    b_factors = list(set(b_factors))

    numbers = intersect(a_factors,b_factors)
    return max(numbers)
    # code goes here 
        
def intersect(a, b):
    return list(set(a) & set(b))
# A function to print all prime factors of  
# a given number n 
def primeFactors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
    
# keep this function call here  
print Division(raw_input())
