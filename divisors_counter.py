n = int(input("Enter an integer: "))

while n <= 0:
    n = int(input("Enter a positive non-null integer: "))

i = 1    

counter = 0

divisors=[]

while i <= n :                
    if n % i == 0 :          
        counter += 1
        divisors.append(i)             
    i += 1                  

print(n, "has", counter, "divisors:", divisors)

