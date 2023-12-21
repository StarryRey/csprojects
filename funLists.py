myList = [ 1,3,5,56,234]
myindex= myList.index( 56)
print ( 'myindex',myindex
       )
sumList = sum( myList)
print ( sumList)
myList.sort(reverse= True)
print( myList)
Mylist= ['zoo', 'app','bait','cycle']
Mylist.sort()
print(Mylist)
Mylist.sort(key=len)
print (Mylist)
Mylist.sort(key=len,reverse=True)
print ( Mylist)
for element in Mylist:
    if ( element== 'zoo'):
        print(element)
    else:
        print( "not found zoo:>")
for num in myList:
    num=num + 1
    print (num)

List = [ 1,2,3,4,5,6,7]
for element in List[:3]:
    List.remove( element)
    print ( 'removing', element)
print ( List)

MyList = []

for element in range(1,10):
    data = element**2
    MyList.append(data)
    print('appending=',data)

print (MyList)

numTuple= (1,2,3,4,5)
print ( (list(numTuple)))
