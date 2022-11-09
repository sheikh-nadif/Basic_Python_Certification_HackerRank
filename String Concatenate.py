def mutate_string(string, position, character):
    s = string
    i = position
    c = character

    return s[:i] + c + s[i+1:] #directly return the string or it will also return none

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)