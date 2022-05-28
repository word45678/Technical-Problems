def ZigZag(phrase, rows):
    if rows < 2:
        return phrase
    mess = [""] * rows
    goingdown = True
    pointer = 0
    spot = 0
    final = ""
    while pointer < len(phrase):
        mess[spot] += phrase[pointer]
        if goingdown:
            spot += 1
        else:
            spot -= 1
        if spot == rows - 1:
            goingdown = False
        if spot == 0:
            goingdown = True
        pointer += 1
    for i in range(rows):
        final += mess[i]
    return final

if __name__ == "__main__":
    test = input("Please enter your test phrase: ")
    row = int(input("Please enter your number of rows: "))
    result = ZigZag(test,row)
    print("Zigzag of your phrase '" + test + "' with " + str(row) + " rows yielded: '" + result + "'")