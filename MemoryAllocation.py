#id ()
data= 10
print (id( data))
item = 10
print (id( item))
if id(data)== id( item):
    print(" They have same id address",id(data),id(item))
else:
    print( "They are not same:>")