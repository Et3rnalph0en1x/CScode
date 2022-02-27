#prelab08 

#Rajesh Balasamy

#CS177

#process file as a list

def readCourses(filename):

    coursesList = []

    infile = open(filename, 'r')

    line = infile.read().splitlines()
    
    for i in range(len(line)):

        line2 = line[i].split(',')

        line2[2] = float(line2[2])
        
        coursesList.append(line2)
    
    infile.close()

    return coursesList

#take average of all grades

def computeAverage(coursesList):

    average = 0

    for i in range(len(coursesList)):

        average = average + coursesList[i][2]

    average = float(average / len(coursesList))

    return average

#main call

if __name__ == "__main__":

    main()
