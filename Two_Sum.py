def twoSumIndices(data,target):
    complements = {}
    for i in range(len(data)):
        complement = target - data[i]
        if(complement in complements.keys()):
            return [complements[complement],i]


numbers = [2,7,11,15]
value = 9
print("Input: " + str(numbers) + " and Target: " + str(value))
print("Sum component locations: " + str(twoSumIndices(numbers,value)))