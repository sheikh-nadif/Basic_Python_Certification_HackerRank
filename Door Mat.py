
row = int(input("input odd number for row value [Example: 1,3,5,....]  "))
column = row*3

#````Alternative Solution`````#

# for i in range (0,int(row/2)): #range in 0,1 int(row/2)= 2 [for row = 5]
    # pattern = ".|." * ((2*i)+1) #1st = (2*0)+1=1, 2nd= (2*1)+1=3
    # print(pattern.center(column, "-")) #center pattern
 # i = int (rows / 2)
    # while i > 0:
       # pattern = "|*|" * ((2 * i) - 1)
       # print (pattern.center (width, '-'))
       # i = i-1

for i in range (1,row,2): #range is 1,3..(n-2) skipped 2 values [range(start, finish, skip)]
    pattern = ".|." * i
    print(pattern.center(column, "-")) #center pattern

print("WELCOME".center(column, "-")) #welcopme in center of pattern

for i in range (row-2,-1,-2):#range is (n-2)...3,1 skipped 2 values in reverse order [range(start, finish, skip)]
    pattern = ".|." * i 
    print(pattern.center(column, "-")) #center pattern
    