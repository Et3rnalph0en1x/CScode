#Pre-lab 7 Q1

#Rajesh Balasamy

#CS177

#main function

def isMultiple(num1, num2):

#counter and "false" returns

    counter = 0

    if num1 <= 0 or num2 <= 0:

        return -1

    for i in range(1, num1+1):

        if i % num2 == 0:

            counter = counter + 1

            print(i)
            
    return counter


#call
    
if __name__ == "__main__":

    main()
    
