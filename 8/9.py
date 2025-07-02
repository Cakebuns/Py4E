try:
    myFile = open(r"C:\Users\keira\OneDrive\Documents\py4e\8\mbox.txt")
except:
    print("rut row, couldn't open")
    exit()
lineCount = 0
senders = dict()
for srcLine in myFile:
    lineCount = lineCount + 1
    tempLine = srcLine.strip()
    if tempLine.startswith('From:'):
        lineWords = templine.split()
        if lineWords[1] not in senders:
            senders[lineWords[1]] = 1
        else:
            senders[lineWords[1]] += 1
for sender in senders:
    senderList = senderList + (sender, senders(sender))
sendersList.sort(key=lambda tup: tup[1])
for sender in senderList:
  print(sender[0] + sender[1])
    

        
