#armstrong numbers
#num = int(input())
num = int(800000000)

for i in range (num):
    check_num = i
    power = len(str(check_num))
    sum = 0
    temp = 0
    while i>0:
        temp = i % 10
        sum = sum + (temp**power)
        i = i//10
    if sum ==check_num:
        #print(str(check_num)+" is not armstrong")
        print(str(sum)+ " armstrong")