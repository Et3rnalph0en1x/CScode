#prelab11

#Rajesh Balasamy

#CS177

#returns a list of lletters that don't occur in both given words

def symmetricDifference(word1, word2):
    
    endList = []
    
    def removeDuplicates(word):
        
        endList = []
        
        for i in word:
            
            if i not in endList:
                
                endList.append(i)
        
        end = sorted(endList)
        
        return end
    
    w1 = removeDuplicates(word1)
    
    w2 = removeDuplicates(word2)
    
    for i in w1:
        
        if i not in w2:
            
            endList.append(i)
            
    for i in w2:
        
        if i not in w1:
            
            endList.append(i)
    
    endList = sorted(endList)
    
    return endList
                  