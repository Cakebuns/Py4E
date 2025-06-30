userZip = input("What is your zipcode:\n")
if (len(userZip) == 5):
    try:
        #firstTwoDigits = int(int(userZip)/1000)
        firstTwoDigits = int(userZip[0:2])
        if ( firstTwoDigits >= 43 and firstTwoDigits <= 45):
            print("you probably live in Ohio")
        
        else:
            print("you probably don't live somewhere nicer than Ohio")
    
    except:
        print("Please only type numbers")
    
else:
    print("Please type a 5 digit zipcode")

