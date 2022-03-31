#prelab11

#Rajesh Balasamy

#CS177

#keepmax

def keepMax(numList):
    
    if (len(numList) == 0):
        
        return -1
    
    endList = [numList[0]]
    
    for i in range(len(numList)):
        
        if i < 0 or (len(numList) == 0):
            
            return -1
        
        if numList[i] > max(endList):
            
            endList.append(numList[i])
        
    return endList
