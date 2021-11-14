#!/usr/bin/env python3
'''
Morning if it's morning 
Evining if it's evining 

Mr12

https://www.hackerrank.com/challenges/nested-list

'''

# Find the seconde lowwer grade 
def findTheSecondLower(sortedRecords):
    result = []
    start = False # True if you removed the duplicated first one
    firstLow = sortedRecords[0] # first element of the array
    for x in sortedRecords[1:]:
        if firstLow[1] == x[1]:
            if start: # if start = True then you start the work 
                result.append(x[0])
            else:
                continue
        elif x[1] > firstLow[1] and not start: # Find the first lowwer 
            firstLow = x
            start =True
            result.append(x[0])
    else:
        return result # after you finsh the loop


# Return the second element of an array
def take2depth(x):
    return x[1]

if __name__ == '__main__':
    records = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19] , ['Vikas',21]]
    sortedByLow = sorted(records,key=take2depth)
    secondLow = findTheSecondLower(sortedByLow)
    for i in sorted(secondLow): print(i)
