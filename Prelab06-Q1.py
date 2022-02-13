#Prelab 06 #1

#Rajesh Balasamy

#CS177

results = []

#function

def factors(myNumber):

    for i in range(1, myNumber + 1):

        if myNumber % i == 0:

            results.append(i)

    return(results)

#call

if __name__ == "__main__":

    main()
