# Task
# Given an integer, n , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If n is even and greater than 20 , print Not Weird


while(True):
       n = int(input().strip())
       check = {True: "Not Weird", False: "Weird"}

       print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ] ) 
