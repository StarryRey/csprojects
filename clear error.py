while True:
    number = input( " Enter digits:>")
    if number.isdigit() and len( number) < 3 and len( number)> 1:
        print ( " It works!!!")
        break
    print ( " Try Again:")
