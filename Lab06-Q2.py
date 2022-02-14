#lab6 Q1

#Rajesh Balasamy

#CS177

def splitAndJoin(myString):

#if statement and elif for odd and even numbered strings

    if len(myString) == 1:

        result = myString

    elif len(myString) % 2 == 0:

        s1 = myString[:len(myString)//2]

        s2 = myString[len(myString)//2:]

        result = s2 + s1

    else:

        s1 = myString[0:len(myString)//2]

        s2 = myString[len(myString)//2]

        s3 = myString[(len(myString)//2)+1]

        result = s2 + s3 + s1

    return(result)

#call

if __name__ == "__main__":

    main()
