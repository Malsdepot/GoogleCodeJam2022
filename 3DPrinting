testCases = int(input())

unitsNeeded = 1000000
outString = ""
for case in range(1, testCases+1):
    outString += (f"Case #{case}: ")
    printer1 = [int(i) for i in input().split()]
    printer2 = [int(i) for i in input().split()]
    printer3 = [int(i) for i in input().split()]
    
    minC = min(printer1[0], printer2[0],printer3[0])
    minM = min(printer1[1], printer2[1],printer3[1])
    minY = min(printer1[2], printer2[2],printer3[2])
    minK = min(printer1[3], printer2[3],printer3[3])
    
    effPrinter = (int(minC), int(minM), int(minY), int(minK))
    if (sum(list(effPrinter)) < unitsNeeded):
        outString += ("IMPOSSIBLE")
    else:
        total = 0
        reached = False
        for colorCart in effPrinter:
            if reached:
                outString += str("0 ")
            else:
                total+=colorCart
                if total <= unitsNeeded:
                    outString+=str(f'{colorCart} ')
                elif total > unitsNeeded:
                    remainder = total - unitsNeeded
                    colorCart-=remainder
                    outString+=str(f'{colorCart} ')
                    reached = True            
    outString+="\n"
print(outString)
