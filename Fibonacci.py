import sys

def PrintFibonacciNumbers(maxNumber):
    secondPrev = 0
    prevNum = 1
    print("1")
    fibonacciNum = 1
    
    while(fibonacciNum < maxNumber):
        fibonacciNum = prevNum + secondPrev
        secondPrev = prevNum
        prevNum = fibonacciNum
        print(str(fibonacciNum))

PrintFibonacciNumbers(100000)