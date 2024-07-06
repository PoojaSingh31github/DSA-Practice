def calculateAverage(numbers):
    n= len(numbers)
    sum=0
    for i in numbers:
        sum+=i
    average=sum/n   
    return average 

Input=[10, 15, 20, 25]  

avr= calculateAverage(Input)
print(avr)