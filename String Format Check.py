# sol with for loop and eval()
if __name__ == '__main__':
    s = input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        x=any(eval("c." + test + "()") for c in s)
        print(x)

# alternative for loop sol
# if __name__ == '__main__':
   # s = input()
    #for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
     #print (any(method(c) for c in s))

# alternative for loop sol with type() and list
# if __name__ == '__main__':
   # s = input()
    #t = type(s)
    #for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
      #print (any(method(c) for c in s))

# direct sol
#print(any([char.isalnum() for char in s]))
#print(any([char.isalpha() for char in s]))
#print(any([char.isdigit() for char in s]))
#print(any([char.islower() for char in s]))
#print(any([char.isupper() for char in s]))