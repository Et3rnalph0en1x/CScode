#CS177

#Raj B

#Week 12

#merges two dictionaries

def mergeDictionaries(dict1, dict2):
    
    endDictionary = dict1
    
    dictKeys = list(endDictionary.keys())
    
    for i in range(len(dictKeys)):
        
        if dictKeys[i] in dict2:
            
            endDictionary[dictKeys[i]] = [endDictionary[dictKeys[i]], dict2[dictKeys[i]]]
            
            del dict2[dictKeys[i]]
    
    endDictionary.update(dict2)
            
    return(endDictionary)
    
#main call

#print(mergeDictionaries({1 : 'a', 2 : 'b'}, {3 : 5, 4 : 6}))
#print(mergeDictionaries({1 : 'a', 2 : 'b'}, {1 : 5, 2 : 6}))
#print(mergeDictionaries({1 : 'a', 2 : 'b'}, {2 : 5}))
#print(mergeDictionaries({1 : [1, 2]}, {1 : [2, 3, 4]}))
if __name__ == "__main__":
    main()
