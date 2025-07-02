try:
    myFile = open(r"C:\Users\keira\OneDrive\Documents\py4e\8\mbox.txt")
except:
    print("rut row, couldn't open")
    exit()
lineCount = 0
senderDict = dict()
for srcLine in myFile:
    lineCount = lineCount + 1
    tempLine = srcLine.strip()
    if tempLine.startswith('From:'):
        lineWords = tempLine.split()
        if lineWords[1] not in senderDict:
            senderDict[lineWords[1]] = 1
        else:
            senderDict[lineWords[1]] += 1
senderList = []
for sender in senderDict:
    senderList.append([sender, senderDict[sender]])
senderList.sort(key=lambda tup: tup[1], reverse=True)
for sender in senderList:
  print(sender[0] + " sent " + str(sender[1]) + " emails")
    

        
