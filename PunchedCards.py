tests = int(input())

def isEven(v:int):
    return v%2

outString = ""
for test in range(1,tests+1):
    outString+=(f"Case #{test}:\n")
    card = list(map(int, input().split()))
    for row in range(card[0]*2+1):
        for column in range(card[1]*2+1):
            if ((row <= 1) and (column <= 1)):
                outString += '.'
            elif(not isEven(row)):
                if(not isEven(column)): 
                    outString +='+'
                else:
                    outString +='-'
            elif(isEven(row)):
                if(not isEven(column)):
                    outString += "|"
                else:
                    outString += "."
        outString+="\n"
print(outString)
