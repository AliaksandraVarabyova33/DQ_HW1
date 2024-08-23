from random import randint

#task1: create list of 100 random numbers from 0 to 1000
n = 100
#empty list is created
randomIntegers = []

#in the cycle for with n iterations random integers from 1 to 1000 are created and added to the end of the list
for i in range(n):
    randomIntegers.append(randint(1,1000))

#task2: sort list from min to max (without using sort())

#outer loop to navigate for the list
for i in range(len(randomIntegers)-1):
    #inner loop to navigate for the list
    for j in range(len(randomIntegers)-1-i):
        #checking if the current element bigger than the next one
        if randomIntegers[j] > randomIntegers[j+1]:
            #if bigger -> swap them
            randomIntegers[j], randomIntegers[j+1] = randomIntegers[j+1], randomIntegers[j]

#task3: calculate average for even and odd numbers
#task4: print both average result in console

#variables for sums and counts are created
evenSum = 0
evenCount = 0
oddSum = 0
oddCount = 0

#visiting each list element
for i in range(len(randomIntegers)):
    #checking if it's even or odd
    if randomIntegers[i]%2 == 0:
        #if remainder of division by two is 0 than it's even, add this number to the even sum, increase even count by 1
        evenSum += randomIntegers[i]
        evenCount += 1
    #else it's odd, add this number to the odd sum, increase odd count by 1
    else:
        oddSum += randomIntegers[i]
        oddCount += + 1
#counting average by dividing sum into count, printing it to console
print('Average for even = ' + str(evenSum/evenCount))
print('Average for odd = ' + str(oddSum/oddCount))

