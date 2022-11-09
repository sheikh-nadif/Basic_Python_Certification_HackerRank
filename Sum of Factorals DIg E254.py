import math
# finding out f(n) values for the input 
# for n = 342, f(n) is :: 3! + 4! + 2! = 32
n = input()
n_int= int(n)
n_length = int(len(n))
print("length of input is: " , n_length)
result_fn = 0
for i in range (n_length):
    dig = n_int % 10
    print("digit is: " , dig)
    
    fac = math.factorial(dig)
    print("factorial is: " , fac)

    n_int = n_int//10
    print("reamin is: " , n_int)

    result_fn = result_fn + fac
    

print("result of f(n) is: " , result_fn)


# finding out sf(n) values for the input 
# for n = 342, f(n) is :: 3! + 4! + 2! = 32
# So, sf(n) = 3 + 2 = 5  

fn_length = len(str(result_fn))
print("length of f(n) is: " , fn_length)
result_sfn = 0

for j in range (fn_length):
    dig = result_fn % 10
    print("digit is: " , dig)

    result_fn = result_fn//10
    print("reamin is: " , result_fn)

    result_sfn = result_sfn + dig
    

print("result of sf(n) is: " , result_sfn)

#from here g(i) values will be calculated
# sf( 1)=s(   1!)=s(     1)=          1=>G( 1)=1
# sf( 2)=s(   2!)=s(     2)=          2=>G( 2)=2
# sf( 3)=s(   3!)=s(     6)=          6=>G( 6)=3
# sf( 4)=s(   4!)=s(    24)=        2+4=>G( 6)=4? No sf( 3)=6.
# sf( 5)=s(   5!)=s(   120)=      1+2+0=>G( 3)=5
# sf( 6)=s(   6!)=s(   720)=      7+2+0=>G( 9)=6
# sf( 7)=s(   7!)=s(  5040)=    5+0+4+0=>G( 9)=7? No sf( 6)=9.
# sf( 8)=s(   8!)=s( 40320)=  4+0+3+2+0=>G( 9)=8? No sf( 6)=9.
# sf( 9)=s(   9!)=s(362880)=3+6+2+8+8+0=>G(27)=9
# sf(10) Same digits are already evaluated by sf(1)
# sf(11) Pairs of 1!+1! are always replacible by 2!
# sf(12)=s(1!+2!)=s(   1+2)=          3=>G( 3)=12? No sf( 5)=3.
# sf(13)=s(1!+3!)=s(   1+6)=          7=>G( 7)=13
# sf(14)=s(1!+4!)=s(  1+24)=        2+5=>G( 7)=14? No sf(13)=7.
# sf(15)=s(1!+5!)=s( 1+120)=      1+2+1=>G( 4)=15

sfn_length = len (str(result_sfn))
print("length of sf(n) is: " , sfn_length)

sg = 0
sum_fac_sfn = 0
for k in range (result_sfn):

    print(k)   
    sfn_dig_fac = math.factorial(k+1)
    print("factorial is: " , sfn_dig_fac)

    sum_fac_sfn = sum_fac_sfn + sfn_dig_fac
    

print("result of f(n) is: " , sum_fac_sfn)
   