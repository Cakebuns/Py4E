largest = None
smallest = None
count = 0
average = 0
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        count = count + 1
        if smallest == None or num < smallest:
            smallest = num
        if largest == None or num > largest:
            largest = num
        if count > 1:
            average = (average*(count - 1) + num) / count
        else:
            average = num
    except:
        print("Hey! thats not an int!  idiot")

print("Maximum        : ", largest)
print("Minimum        : ", smallest)
print("Number of items: ", count)
print("Average        : ", average)
