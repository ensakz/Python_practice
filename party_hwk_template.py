'''
Let's party problem


Your friend visits you and says he has an invitation to a party
at which there will be celebrities.  He is very excited by the
prospect of meeting famous people.  However, he has a problem.
These celebrities are going to attend the party at different time
periods. For example two individuals may attend the party for three
hours but these may be at non overlapping intervals.
Even though he knows when each celebrity will be attending,
your friend is not able to figure out when to attend the party such
that he meets the most number of celebrities.  The problem is also that he
has only 59 minutes to attend the party given the approaching finals week.

You say Aha!  I can write a program that gets a solution for you.
Tell me when each celebrity is going to be at the party and my
program will tell you what's the best time to
visit the party.

Assume a 24 hour clock and at least 5 celebrities

Assume that the durations always start on the hour and end just
before an hour. For example, a celebrity may enter the party at 11
and leave just before 14 hours. This means the person has been there
for just short of three hours.  Individuals cannot enter at other times
or leave at other times.  This holds for your friend as well.
Assume too that each celebrity attends the party only once.

Write a program that tells your friend which hour is the best in which to
join the party given each celebrity's entry and exit hours.

Two basic questions as always.

How to represent the problem?

I wrote 3 main functions for this program which are 
1. getnumberofguests() which allows user to input the number of celebrities who will come to the party
2. guest_hours() which takes returned output from function 1 and allows user to input hours at which every guest will enter the party. 
I believe that asking only entry hours is more convenient for my friend as we already know that all guests will stay fixed amount of time (3 hours) 
so it is not required to ask when they leave the party.
3. hourtoattend() which takes returned output from function 2 and prints out time to attend when you can meet the most celebrities.

How to solve the problem?

I solved the problem by first creating list to store number of celebrities who will come to the party. Then, I loop through each celebrity and 
create new list with hour time when each celebrity will be at party. Finally, I select hours when the biggest number of celebrities will be at
party and check whether these hours are in sequence, ie represent a longer time period than 1 hour. After that, I select time period with longest duration
and print a suggesting message to attend party at that time.

Assumptions:
1. My program will work for any number of guests but it does satisfy the requirement of at least 5 guests coming to the party.


'''
from statistics import mode, multimode

def main():
    step1= getnumberofguests()
    step2 = guest_hours(step1)
    step3 = hourtoattend(step2)

#creates list with number of guests by asking user to input guest information
def getnumberofguests():
    try:
        guests = int(input('How many celebrities will attend party? '))
    except:
        while True:
            try: 
                guests = int(input("Please input number of participating celebrities using integers: ")) 
                if type(guests) == int: 
                    break
            except: 
                continue
    #list where all hours when celebrity come to the party will be stored
    guests = [guest+1 for guest in range(guests)]
    return guests

#assigns participating party hours for each guest
def guest_hours(guests):
    periods = []
    for guest in guests:
        try:
            while True:
                period_, period2_=input("Please indicate hours when celebrity number " + str(guest) + \
                " will come and leave the party (enter two integers from 0 to 23 separated by white space): ").split()
                period = int(period_)
                period2 = int(period2_)
                #print(type(period))
                if period < 24 and period >= 0 and period2 < 24 and period2 >= 0:
                    break
                else:
                    continue
        except:
            while True:
                try:
                    period_, period2_=input("Please indicate hours when celebrity number " + str(guest) + \
                    " will come the party (enter two integers from 0 to 23 separated by white space): ").split()
                    period = int(period_)
                    period2 = int(period2_)
                    #print(type(period))
                    if period < 24 and period >= 0 and period2 < 24 and period2 >= 0:
                        break
                except:
                    continue
        #creates a list with participating hours for each guest
        list_to_add= list(range(period, period2))
        periods.extend(list_to_add)
    return(periods)

#print the best time to meet the most guests at party
def hourtoattend(periods):
    #situation when nobody comes at the same time or present at the same time
    if len(set(periods)) == len(periods):
        #sort guest coming hours to check whether they coming 1 hour after another or not, ie in sequence, ex: [0, 1, 2, 3]
        periods_sorted = sorted(periods)           
        stop = len(periods_sorted) - 1
        h = 0
        i = 1
        #range_ list which stores continuous time periods when guest come one after another
        range_ = []
        while i < len(periods_sorted):
            value_1 = periods_sorted[i-1]
            value_2 = periods_sorted[i]
            if i == stop:
                #print(h)
                #print(i)
                if value_2 - value_1 == 1:
                    range_.append([h, i])
                elif value_1 - periods_sorted[i-2] == 1:
                    range_.append([h, i-1])
                    range_.append([i])
                else:
                    range_.append([h])
                    range_.append([i])
                break
            elif value_2 - value_1 == 1:
                i += 1
            else:
                if i == 1:
                    range_.append([h])
                    h = i
                    i += 1
                else:
                    range_.append([h, i-1])
                    h = i
                    i += 1

        #if guests are coming one after another where all time intervals are exacly 1 hour, ex.[0,1,2,3,4,5]
        if len(range_) == 1:
            #print("chec")
            #modular turns 24 hours into 0 hours
            if periods_sorted[range_[0][0]] == (periods_sorted[range_[0][1]]+1):
                print("You can come any hour of the day")
            else:
                print("You can come to the party to meet celebrities from " + str(periods_sorted[range_[0][0]]) + " to " + str((periods_sorted[range_[0][1]])) + " hours.")
            
        #if guest are not coming one after another and there are gaps more than 1 hour between their coming times
        else:
            #count time intervals of sublists which have len>1
            #print("check")
            count = [[el[1] - el[0], el] for el in range_ if len(el) > 1]
            #select biggest intervals from sublists
            most_celeb_interval = [el[1] for el in count if max(count, key=lambda x: x[0])[0] == el[0]]
            for int_ in most_celeb_interval:
                #print biggest intervals where you can visit guests
                #print(periods_sorted[int_[0]], periods_sorted[int_[1]])
                print("You can come to the party to meet celebrities from " + str(periods_sorted[int_[0]]) + " to " + str((periods_sorted[int_[1]])) + " hours.")
    #situation when some celebrities come at the same time or present at the same time
    else:
        #select most frequent time periods
        hour = multimode(periods)
        #print("bla")
        #situation when only 1 particular hour is frequent
        #print(hour)
        if len(hour) == 1:
            #print("hi")
            #print(hour[0])
            print("You can come to the party to meet celebrities at " + str(hour[0]) + " hours.")
        #need to check whether multiple hour entries are continuous or not via recursion
        else:
            hourtoattend(hour)
main()
