def reverseIntStr(num):
    #with converting to a string
    negative = num<0
    temp = num
    if negative:
        temp = temp*-1
    temp = str(temp)
    final = ""
    for i in range(len(temp)):
        final += temp[len(temp)-i-1]
    if negative:
        final = "-"+final
    return int(final)

def reverseInt(num):
    #without converting to a string
    negative = num<0
    temp = num
    final = 0
    if negative:
        temp = temp*-1
    while temp % 10:
        final = final * 10
        final += temp % 10
        temp = int(temp / 10)
    if negative:
        final = final * -1
    return final


if __name__ == "__main__":
    test = input("Please enter your integer: ")
    result = reverseInt(int(test))
    print("Reverse of your number: " + test + " yielded " + str(result) + "")