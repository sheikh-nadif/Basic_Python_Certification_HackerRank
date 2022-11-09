# Given a Number:
# if multiple of 3 and 5 print "FizzBuzz"
# if multiple of only 3 print "Fizz"
# if multiple of inly 5 print "Buzz"
# else print i (iteration value)

def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print ("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print ("Buzz")
        else:
            print (i)

print(fizzBuzz(n))