def longSubStr(phrase):
    longest = ""
    length = 0
    substrings = {}
    for i in phrase:
        if i in longest:
            substrings[length] = longest
            longest = i
            length = 1
        else:
            longest += i
            length += 1
    substrings[length] = longest
    return substrings[max(substrings.keys())]

if __name__ == "__main__":
    spork = input("Please input your string: ")
    result = longSubStr(spork)
    print("In '" + spork + "' the longest unique character substring is of length " + str(len(result)) + " and is '" + result + "'")