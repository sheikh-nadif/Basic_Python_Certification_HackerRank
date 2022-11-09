# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

def count_substring(string, sub_string):
    count = 0
    i = string.find(sub_string)
    #print("i is ",i)
    while i != -1:   # if substring not availabe string.find() will return -1, 
                     # remove (#) on the print functions for better understanding
        count += 1
        i = string.find(sub_string, i+1)
        #print("i is ",i)
    return count

string = "abcdcdc"
sub_string = "cdc"
    
count = count_substring(string, sub_string)
print (count)




#best solution::::Using startswith() method

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count

string = "abcdcdc"
sub_string = "cdc"
count = count_substring(string, sub_string)
print (count)




# alternative solution without function
# string, substring = ("abcdcdc","cdc")
# print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))
