def sortDie(dieCollection):
    straight = 0
    for i in range(len(dieCollection)):
        if i < dieCollection[i]:
            straight +=1

    if straight < len(dieCollection):
        dieCollection.pop(0)
        straight = sortDie(dieCollection)
    return straight

testCases = int(input())
outString = ""
for case in range(1,testCases+1):
    outString += (f"Case #{case}: ")
    numDice = int(input())
    dieCollection = [int(i) for i in input().split()]
    dieCollection.sort()
    straight = sortDie(dieCollection)
            
    outString+=(f"{straight}\n")
print(outString)
