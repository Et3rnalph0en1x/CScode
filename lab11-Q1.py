#rajesh balasamy

#cs177

#lab11

#determines the amount of times an element occurs in these 3 lists

def uniqueOccurrence(list1, list2, list3):
    
    combine = sorted(list1 + list2 + list3)
    
    endList = {}
    
    def removeDuplicates(word):
        
        list2 = []
        
        for i in word:
            
            if i not in list2:
                
                list2.append(i)
        
        end = sorted(list2)
        
        return end

    unique = removeDuplicates(combine)

    for j in range(len(unique)):

        endList[unique[j]] = combine.count(unique[j])
        
    return(endList)

#main call

if __name__ == "__main__":
    main()

