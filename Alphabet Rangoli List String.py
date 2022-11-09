# Width Logic
# input  + input - 1 + ((input + input -1)-1)
# Example: input = 5 (e-d-c-b-a-b-c-d-e)
# alphabets number will be: 5+5-1 =9
# hyphens will be: (5+5-1)-1 = 8
#So, Width = input * 4 - 3

# for, input = n = 5
# 0     1       2       3       4
# a     b       c       d       e
# n-5   n-4     n-3     n-2     n-1


#for i in range(1,n+1) [Print Upper Half]

                    #--------e--------
                    #------e-d-e------
                    #----e-d-c-d-e----
                    #--e-d-c-b-c-d-e--
                    #e-d-c-b-a-b-c-d-e
                    #--e-d-c-b-c-d-e--
                    #----e-d-c-d-e----
                    #------e-d-e------
                    #--------e-------- 

# left-upper-triangle               right-upper-triangle
# n-1:n-1:-1                        n-1:n 
# n-1:n-2:-1                        n-2:n
# n-1:n-3:-1                        n-3:n
# n-1:n-4:-1                        n-4:n
# So, 
# n-1:n-i:-1                        n-i:n


# for i in range(n-1,0,-1) [Print Lower Half]
# -1 for reverse order
# ######

import string

L = [] #List

def print_rangoli(size):

    n = size
    width = n * 4 - 3

    char = string.ascii_lowercase
    for i in char:
        L.append(i) #inputting a-z in list

    for i in range (1,n+1): 
    # range 1,n+1 indicates loop size (1-5 : e-a)
    # range only n will print 1 empty list once
        print("-".join(L[n-1:n-i:-1]+L[n-i:n]).center(width,"-")) 
    for i in range (n-1,0,-1):
    # range n-1,0 indicates loop size (4-1 : b-e)
    # range only n or n,1 will print n=5 twice or n=0 : e will not print at end
        print("-".join(L[n-1:n-i:-1]+L[n-i:n]).center(width,"-"))
size = int(input())
print_rangoli(size)