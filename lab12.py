#CS177 - lab12.py

#Raj B

#Week 12

#merges two dictionaries

def readStudents(filename):
    
    studentsDict = {}
    
    myfile = open(filename, 'r')
        
    for line in myfile:
            
        key, value = line.strip().split(',')
            
        studentsDict[key.strip()] = value.strip()
    
    return(studentsDict)

def readGrades(filename):
    
    gradesList = []
    
    myfile = open(filename, 'r')
    
    for line in myfile:
        
        x,y,z = (line.strip().split(','))
        
        z = int(z)
        
        temp = [x,y,z]
        
        gradesList.append(temp)
    
    return(gradesList)


def finalGrades(studentsDict,gradesList):
    
    keys = list(studentsDict.keys())
    
    finalDict = {}
    
    for i in range(len(keys)):
        
        count = 0
        
        total = 0
        
        for j in range(len(gradesList)):
            
            if gradesList[j][1] == keys[i]:
                
                count = count + 1
                
                total = total + gradesList[j][2]
                
        temp = [count, total]
        
        student = studentsDict[keys[i]]
        
        finalDict[student] = temp
    
    return(finalDict)



if __name__ == "__main__":
    main() 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    