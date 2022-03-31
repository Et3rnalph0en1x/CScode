#rajesh balasamy

#cs177

#lab11

#determines the number of different list elements in 2 lists
def calcListDiff(list1, list2):

    def removeDuplicates(word):
        
        list2 = []
        
        for i in word:
            
            if i not in list2:
                
                list2.append(i)
        
        return list2

    word1 = removeDuplicates(list1)

    word2 = removeDuplicates(list2) 
            
    for i in range(len(word1)):
        
        if word2.count(word1[i]) > 0:

            word2.remove(word1[i])

            word1.remove(word1[i])

            i = i - 1


    if (len(word1)) > (len(word2)):

        diff = len(word1) + len(word2)

    else:

        diff = len(word2) + len(word1)
        
    return(diff)

    
#main call

if __name__ == "__main__":
    main()

