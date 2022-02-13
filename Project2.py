#CS 177 – project02.py

#Rajesh Balasamy

#In project 2, you need to write 7 functions and the main(). These functions, but for main(), will take parameters and may return (or print) values.



#function number 1 uses if loop and balance variable

def judgeBalancingOfWorkout(weightlifting, running):

    balance = weightlifting/20 - running/100 

    if -10 < balance < 10:

        return('yes')

    else:

        return('no')

#function 2 uses the calories variable and a >= comparator
        
def judgeGoodCaloriesBurning(weightlifting, running, streching):

    calories = streching * 10 + running * 100 + weightlifting * 2

    if calories >= 500:

        return('yes')

    else:

        return('no')

#function 3 initializes the given variables and uses and statements

def judgeAchievedGoal(weightlifting, running, streching):

    goalStreching = 50

    goalRunning = 20

    goalWeightLifting = 40

    if ((streching >= goalStreching) and (running >= goalRunning) and (weightlifting >= goalWeightLifting)):

        return('yes')

    else:

        return('no')

#function 4 uses or comparators 
    
def judgeMissingOfWorkout(weightlifting, running, streching):

    if ((streching == 0) or (running == 0) or (weightlifting == 0)):

            return('yes')

    else:

        return('no')

#function 5 uses a > comapator for streching
    
def judgeShortOfStretching(streching):

    if streching < 30:

        return('yes')

    else:

        return('no')

#function 6 uses a greater than comparing method for weightlifting

def judgeTooManyWeightLiftings(weightlifting):

    if weightlifting > 100:

        return('yes')

    else:

        return('no')

#ratind decision uses several if statements that call earlier functions and if they return yes, badges or function is incremented by one.
    
def ratingDecision(weightlifting, running, streching):

    badges = 0

    feedback = 0

    stars = 0

    if judgeBalancingOfWorkout(weightlifting, running) == ('yes'):

        badges += 1

        print('BADGE - Your workout between strength enhancing and running are well balanced')

    if judgeGoodCaloriesBurning(weightlifting, running, streching) == ('yes'):

        badges += 1

        print('BADGE - You consumed more than 500 kcals')

    if judgeAchievedGoal(weightlifting, running, streching) == ('yes'):

        badges += 1

        print('BADGE - You achieved the goals in all of three workouts')

    if judgeMissingOfWorkout(weightlifting, running, streching) == ('yes'):

        feedback += 1

        print('FEEDBACK - Do not miss any of type of workout')

    if judgeShortOfStretching(streching) == ('yes'):

        feedback += 1
 
        print('FEEDBACK - Lack of stretch will make you injured')

    if judgeTooManyWeightLiftings(weightlifting) == ('yes'):

        feedback += 1

        print('FEEDBACK - Too much burden from weightlifting may make you injured')

    if (badges == 0 and feedback == 3):

        print('Rating: one star - Cheer up')

        stars = 1
    
    elif (badges == feedback):

        print('Rating: three stars - Nice')

        stars = 3

    elif (badges > feedback and feedback != 0):

        print('Rating: four stars - Great')

        stars = 4

    elif (badges == 3 and feedback == 0):

        print('Rating: five stars - Awesome')

        stars = 5

    elif (badges < feedback and badges != 0):
        
        print('Rating: two stars - Good')

        stars = 2
    
def main():

    running = int(input('What is your running statistic? '))

    streching = int(input('What is your streching statistic? '))

    weightlifting = int(input('What is your weightlifting statistic? '))

    ratingDecision(weightlifting, running, streching)

    print('your stretching record in minutes: ', streching)

    print('your running record in miles: ', running)

    print('your weightlifting record of counts: ', weightlifting)

    
        
if __name__ == "__main__":

    main()
