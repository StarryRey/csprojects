import secrets
SecureNumber = secrets.SystemRandom()

while True:
    print( "__Welcome to our game_____")
    start =  int(input(" Please press 1 to read the rule or press 2 to play the game:>"))
    if start == 1:
        print(":>Age must be more than 14:")
        print(":> Show money more than $5000:")
        print(":> You must use at least 500 each time:")

    if start == 2:
            Name = input("Your name:>")
            Age = int(input(" Your age:>"))
            while len(Name) > 2 and Age > 17:
                print(" You can play game now:>")
                print ( "Welcome:>", Name)
                break
            print (" Please read again the rules!")

            while True:
                sMoney = int(input("Please enter ur show money:>"))
                while sMoney > 4999:
                    while True:
                        print(" This is ur show money:>", sMoney)
                        inputMoney = int(input(" Please enter your money to play:>"))
                        luckynumber = int(input(" Please enter your luckynumber:>"))
                        systemNumber = SecureNumber.randint(10, 20)

                        while True:

                            print ( "The luckynumber is:>",luckynumber)
                            print ( "The systemNumber is:>",systemNumber)
                            sMoney = sMoney - inputMoney
                            print ( "This is ur money",sMoney)
                            if sMoney < 500:
                                print ("")


                            while luckynumber == systemNumber:
                                print ( " Congrats!"" You win the game")
                                break

                            print( " Wrong Number!"" Please try again")
                            break
                    print ( " Please more money")
    print ( " Please read again the rules")















