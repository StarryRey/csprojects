#namespace 
#Global , Local, Builtin

from math import log2, log10,log1p
a=20
def outerfun():
   print(a)
   a=20
   b=30 # local namespace
def innerFun():
   print (a)
   id(a)
   a=30