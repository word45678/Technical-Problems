def FizzBuzz(number):
    #print FizzBuzz if the number is divisible by both 3 and 5
    #just fizz if its only divisible by 3, just buzz for 5
    #just the num if none
    if number%3==0 and number%5==0:
        return "FizzBuzz"
    elif number%3==0:
        return "Fizz"
    elif number%5==0:
        return "Buzz"
    else:
        return str(number)


if __name__ == "__main__":
    tests = input("Please input an integer: ")
    print(FizzBuzz(int(tests)))
    print("Wasn't that fun...")