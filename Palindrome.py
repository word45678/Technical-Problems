def palinTest():
    phrase = input("Enter your phrase: ")
    simple = ''.join(i for i in phrase if i.isalnum())
    for i in range(int(len(simple)/2)):
        if(simple[i]!=simple[len(simple)-i-1]):
            print('"' + simple + '"' + " is not a palindrome.")
            return
    print('"' + simple + '"' + " is a palindrome.")
    return

palinTest()
cont = input("Run again? (y/n): ")
while cont == "y":
    palinTest()
    cont = input("Run again? (y/n): ")