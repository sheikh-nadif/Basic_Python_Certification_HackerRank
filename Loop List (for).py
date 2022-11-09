list= ["apple", "malta", 6, 9, "cattle", 10, 2, 1]
for item in list:
    if str(item).isnumeric() and item > 6:
        print(item)