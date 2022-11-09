#n = int(input())
n=7
num = 64
for row in range(n):
    for column in range(0,row+1):
        ch = chr(num)
        num = num +1
        print(ch, end='')
        #print("* ", end="")
    print("\r")