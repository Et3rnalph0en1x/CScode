#lab6 Q1

#Rajesh Balasamy

#CS177

def predict(currentPrice, fixedDailyIncreaseRatio):

    endValue = currentPrice * 5

    days = 1

#while loop

    
    while currentPrice <= endValue:

        days = days + 1

        currentPrice = currentPrice * (1 + fixedDailyIncreaseRatio)

        

    return(days)

    


#call

if __name__ == "__main__":

    main()
