from collections import OrderedDict
# Syntax of dict = {'key': value}
mydict = {}

# Infinite loop with break
while True:
    try:
        item = input().upper()
        # Search if item matches a key inside the dict
        if item in mydict:
            mydict[item] = mydict[item] + 1
        else:
            mydict[item] = 1
    except EOFError:
         # https://docs.python.org/3/library/collections.html#collections.OrderedDict
             
        mydict = OrderedDict(sorted(mydict.items(), key=lambda t: t[0]))
        for i in mydict:
            print(mydict[i], i)
        break
