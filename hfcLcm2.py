numLarge = int(input("Enter the largest number"))
numSmall = int(input("Enter the smallest number"))

while(numSmall):
    totalNum = numSmall
    numSmall = numLarge % numSmall
    numLarge = totalNum
print("Here is the HFC",numLarge)
    