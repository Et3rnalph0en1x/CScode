#prelab09 

#Rajesh Balasamy

#CS177

#reads data from a file about countries

import matplotlib.pyplot as pyplot


def readCountriesData(filename):

    countriesList = []

    relativeSizeList = []

    infile = open(filename, 'r')

    line = infile.readlines()

    for i in range(1,len(line)):

        line2 = line[i].split(',')

        countriesList.append(line2[0])

        relativeSizeList.append(float(line2[1]))
        
    return(countriesList, relativeSizeList)



def plotPieChart(countriesList, relativeSizeList):

    labels = countriesList
    
    sizes = relativeSizeList
    
    print(sizes)
    
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','brown','yellow']
    
    pyplot.pie(sizes, labels = labels, colors = colors,shadow=True,normalize=True,autopct='%1.1f%%')
    
    pyplot.legend(loc = 'lower right')
    
    pyplot.axis('equal')

    pyplot.savefig(r'C:\Users\Rajesh\Downloads\plotPieChart.pdf')

#main call

if __name__ == "__main__":

    main()






    
    main()