def PalinInt(num):
    #without converting to a string
    negative = num<0
    temp = num
    final = 0
    if negative:
        temp = temp*-1
    while temp % 10:
        spot = temp % 10
        final = (final * 10) + spot
        temp = int(temp / 10)
    if negative:
        final = final * -1
    return final==num

if __name__ == "__main__":
    test = input("Please enter your integer: ")
    result = PalinInt(int(test))
    print("Reverse of your number: " + test + " yielded " + str(result) + "")