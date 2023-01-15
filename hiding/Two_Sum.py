def twoSumIndices(data,target):
    complements = {}
    for i in range(len(data)):
        complement = target - data[i]
        if(complement in complements.keys()):
            return [complements[complement],i]
        complements[data[i]] = i

def twoSumValues(data,target):
    complements = {}
    for i in range(len(data)):
        complement = target - data[i]
        if(complement in complements.keys()):
            return [complement,data[i]]
        complements[data[i]] = i


if __name__ == "__main__":
    numbers = [2,7,11,15]
    value = 9
    print("Input: " + str(numbers) + " and Target: " + str(value))
    print("Sum component locations: " + str(twoSumIndices(numbers,value)))
    print("Sum component values: " + str(twoSumValues(numbers,value)))