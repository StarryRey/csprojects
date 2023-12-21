import random
myNum = random.randrange ( 11)
chance = 5
print ( "myNum is between 1 to 10")
print ( "you have", chance, " chance")


userNum= int( input(" Enter your number:"))

while userNum != myNum and chance > 1:
    print ( " Sorry! Wrong answer, you must enter a digit between 1 to 10")

    if userNum > myNum :
        print ( "Your number is greater")

    elif userNum > myNum:
        print ( " Your number is smaller")
        print ( "*********")
print ( "you have", chance, " chance")
userNum = int( input( "Guess the number"))
chance -= 1

if userNum == myNum:
    print ( " Congrats! You reach level")
   else:
    print ( " Game over")
    print ( " myNum is", myNum)