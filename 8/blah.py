try:
    myFile = open(r"C:\Users\keira\OneDrive\Documents\py4e\8\mbox.txt")
except:
    print("rut row, couldn't open")
    exit()
count = 0
for srcLine in myFile:
    tempLine = srcLine.strip()
    if tempLine.startswith('From:'):
        print(tempLine)



    
