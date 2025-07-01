def myFirstFunct(a, b):
    try:
        if (a > b):
            return a
        else:
            return b
            
    except:
        print("beep boop, something happened")
        
print(myFirstFunct(input("First num: "),input("Sec num: ")))