#project3

#Rajesh Balasamy

#CS177

#analyzes text about customer and purchase data

import matplotlib.pyplot as pyplot

#returns customerData text file as a list with each line as an entry

def readCustomerData(filename):
    
    customerList = []
    
    infile = open(filename, 'r')

    line = infile.read().splitlines()

    for i in range(len(line)):
        
        tempList = []
        
        line2 = line[i].split(',')
        
        for j in range(len(line2)):
            
            tempList.append(str(line2[j]))

        customerList.append(tempList)
        
    return(customerList)

#returns transactionData text file as a list with each line as an entry
    
def readTransactionData(filename):
    
    transactionList = []
    
    infile = open(filename, 'r')

    line = infile.read().splitlines()

    for i in range(len(line)):
        
        tempList = []
        
        line2 = line[i].split(',')
        
        for j in range(len(line2)):
            
            if j == 2:
                
                tempList.append(int(line2[j]))
            
            else:
            
                tempList.append(str(line2[j]))

        transactionList.append(tempList)
        
    return(transactionList)

#returns productData text file as a list with each line as an entry
    
def readProductData(filename):
    
    productList = []
    
    infile = open(filename, 'r')

    line = infile.read().splitlines()

    for i in range(len(line)):
        
        tempList = []
        
        line2 = line[i].split(',')
        
        for j in range(len(line2)):
            
            if j == 2:
                
                tempList.append(float(line2[j]))
            
            else:
            
                tempList.append(str(line2[j]))

        productList.append(tempList)
        
    return(productList)

#returns the number of customers from a specific state
    
def countCustomers(customerList, category, state):
    
    counter = 0
    
    for i in range(len(customerList)):
    
        if customerList[i][2] == category:
            
            if customerList[i][3] == state:
                
                counter = counter + 1
              
    print(counter)
    
#returns the names of customers that have purchased over 4000 dollars worth of any product
    
def HighValueCustomers(customerList, productList, transactionList):
    
    valueList = []
    
    sortedCustomerList = sorted(customerList)
    
    sortedTransactionList = sorted(transactionList)
    
    sortedProductList = sorted(productList)
    
    for i in range(len(sortedCustomerList)):
        
        moneySpent = 0
        
        for j in range(len(sortedTransactionList)):
            
            if sortedCustomerList[i][0] == sortedTransactionList[j][0]:
                
                for k in range(len(sortedProductList)):
                    
                    if sortedTransactionList[j][1] == sortedProductList[k][0]:
                
                        moneySpent = moneySpent + (sortedTransactionList[j][2] * sortedProductList[k][2])
    
        if moneySpent > 4000:
            
            valueList.append(sortedCustomerList[i][1])
            
    valueList = sorted(valueList)
    
    return(valueList)

#returns the monthly earnings for a specific month
    
def monthlyEarnings(transactionList, productList, month):
    
    earnings = 0
    
    for i in range(len(transactionList)):
        
        if transactionList[i][3] == month:
            
            for j in range(len(productList)):
                
                if transactionList[i][1] == productList[j][0]:
                    
                    earnings = earnings + (transactionList[i][2] * productList[j][2]) 
    
    earnings = round(earnings, 2)
    
    return(earnings)

#returns the numbers of purchases from states that have bought a specific product
    
def stateCategoryStatistics(customerList, transactionList, productList, productCategory):
    
    statesCountList = []
    
    tempStatesCount = []
    
    checkList = []
    
    sortedCustomerList = sorted(customerList, key=lambda category:category[3])
        
    for j in range(len(productList)):
        
        if (productList[j][1] == productCategory):
            
            checkList.append(productList[j])
            
    for l in range(len(sortedCustomerList)):
        
        for i in range(len(transactionList)):
            
            if transactionList[i][0] == sortedCustomerList[l][0]:
        
                for k in range(len(checkList)):
            
                    if transactionList[i][1] == checkList[k][0]: 
                        
                        tempStatesCount.append(sortedCustomerList[l][3])
            
    sortedTempStatesCount = sorted(tempStatesCount)
    
    for m in range(1,len(sortedTempStatesCount)):
        
        if (sortedTempStatesCount[m] != sortedTempStatesCount[m-1]) or (m == len(sortedTempStatesCount)-1):
            
            tempList = []
            
            counter = sortedTempStatesCount.count(sortedTempStatesCount[m-1])
            
            tempList.append(sortedTempStatesCount[m-1])
            
            tempList.append(counter)
            
            statesCountList.append(tempList)
                
    return(statesCountList)

#creates a pie chart using monthlyEarnings function
    
def plotPieChart(transactionList, productList):
        
    janEarnings = monthlyEarnings(transactionList, productList, 'Jan')
    
    febEarnings = monthlyEarnings(transactionList, productList, 'Feb')
    
    marEarnings = monthlyEarnings(transactionList, productList, 'Mar')
    
    labels = ['Jan', 'Feb', 'Mar']
    
    sizes = [janEarnings, febEarnings, marEarnings]
    
    colors = ['tomato', 'lightgreen', 'gold']
    
    pyplot.pie(sizes, colors = colors,autopct='%1.1f%%', startangle=90)
    
    pyplot.legend(labels, loc = 'lower left')
    
    pyplot.axis('equal')

    pyplot.savefig(r'C:\Users\Rajesh\Downloads\plotPieChart.pdf')
    
#creates a bar chart using stateCategoryStatistics function
    
def plotBarChart(statesCountList):
    
    x = []
    
    y= []
    
    z = []
    
    for i in range(len(statesCountList)):
        
        x.append((i+1)*2)
        
        z.append(statesCountList[i][0])
        
        y.append(statesCountList[i][1])
    
    pyplot.bar(x, y, color = 'red')
    
    pyplot.title('State Statistics')
    
    pyplot.xticks(x,z,rotation=345)
    
    pyplot.ylabel('# of customers')
    
    pyplot.savefig(r'C:\Users\Rajesh\Downloads\plotBarChart.pdf')
    
    
#customerList = readCustomerData(r'C:\Users\Rajesh\Downloads\customerData.txt')

#transactionList = readTransactionData(r'C:\Users\Rajesh\Downloads\transactionData.txt')

#productList = readProductData(r'C:\Users\Rajesh\Downloads\productData.txt')

#countCustomers(customerList, 'Individual', 'Minnesota')

#highValueCustomers(customerList, productList, transactionList)

#monthlyEarnings(transactionList, productList, 'Feb')

#statesCountList = stateCategoryStatistics(customerList, transactionList, productList, 'Diodes')

#plotPieChart(transactionList, productList)

#plotBarChart(statesCountList)

if __name__ == "__main__":
    
    main()

