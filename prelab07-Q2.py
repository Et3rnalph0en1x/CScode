#Pre-lab 7 Q2

#Rajesh Balasamy

#CS177

#main function

def substitutePairs(myString, pairsList):

    letters = list(myString)

    for i in range(len(letters)):

           for j in range(len(pairsList)):

               if letters[i] == pairsList[j][0]:

                   letters[i] = pairsList[j][1]
    
    finalWord = ''.join(map(str, letters))

    return finalWord
             

#call
    
if __name__ == "__main__":

    main()
