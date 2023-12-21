# Special Operator
# Identity Operator is and is not ,memory location
 # Membership Operator

a=23
b=24
c= a is b #memory location
print( c)
if a is not b:
    print ("They are same location:>")
else:
    print ("They are not same location:>" )
a=24
if a is not b:
    print ("They are same location:>")
else:
    print ("They are not same location:>" )

s1 = "hello"
s2 = "hello"
s3= s1 is s2
print ("The output is",s3 )
if s1 is s2:
    print ( "They are same",id(s1),id(s2),id(s3))
else:
    print( "They are not same",id(s1),id(s2),id(s3))
    

    
