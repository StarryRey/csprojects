for i in range(5):
    print ('_________')
    try:
        z= 10/(i-3)
        print ('z=',z)
    except ZeroDivisionError:
        print ( " Divided by Zero:")
    finally:
        print ( " always run:>")
    print (i)
