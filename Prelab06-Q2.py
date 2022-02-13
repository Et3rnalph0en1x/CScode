#Prelab 06 #1

#Rajesh Balasamy

#CS177

#function
def changeLetterCase(wordsList):

    results = []

    for i in range(len(wordsList)):

            x = wordsList[i].swapcase()

            results.append(x)

    return(results)

if __name__ == "__main__":

    main()
                        
