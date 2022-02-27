#prelab08 

#Rajesh Balasamy

#CS177

#reads input file and returns list of lists

def readSalesData(filename):

    salesData = []

    infile = open(filename, 'r')

    line = infile.read().splitlines()
    
    for i in range(len(line)):

        line2 = line[i].split(',')

        for j in range(len(line2)):

            if j != 0:

                line2[j] = float(line2[j])
        
        salesData.append(line2)
    
    infile.close()

    return salesData

#computes average until a negative value is encountered

def computeAverageSales(salesData):

    endList = []

    for i in range(len(salesData)):

        tempList = []

        average = 0

        counter = 0

        tempList.append(salesData[i][0])

        for j in range(len(salesData[i])):

            if j > 0:
                
                if salesData[i][j] < 0:

                    break

                average = average + salesData[i][j]

                counter = counter + 1

        average = average / counter

        tempList.append(average)

        endList.append(tempList)
    
    endList = sorted(endList, key=lambda x:x[0])
    
    return endList

#main call

if __name__ == "__main__":

    main()












                    
    
