# Given a string. Split the string on a   (space) delimiter and join using a - hyphen. 

def split_and_join(line):
    # write your code here
    line = line.split()
    new_line= "-".join(line)
    return new_line


line = input()
result = split_and_join(line)
print (result)