#pyramid triangle python
row =int(input(" Please enter your pyramid size:>"))
size = row


for i in range(row):
    for z in range(1,size):
        print ( end='')

    size= size-1

    for j in range(1,(i*2)):
        print( '*',end = '')
    print ( '')