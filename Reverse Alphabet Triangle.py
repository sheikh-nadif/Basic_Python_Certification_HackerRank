#n = int(input())
n = 5
end_range = 65 + 5
# outer loop
for i in range (65, end_range):
    x = end_range
    # inner loop
    for j in range(65,i+1):
       # n = n - 1
        x-=1
        print("-"+chr(x),end="-")
        
    print()