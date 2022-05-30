def myAtoi(given):
    final = ""
    negative = False
    numbers = True
    for i in given:
        if i.isnumeric() and numbers:
            final+=i
        elif i=="-":
            negative = True
        elif i.isspace(): pass
        else:
            numbers = False
            break
    final = int(final)
    if negative:
        final = final *-1
    return final

if __name__ == "__main__":
    test = input("Please enter your string: ")
    result = myAtoi(test)
    print("Read of your string: " + test + " yielded: " + str(result))