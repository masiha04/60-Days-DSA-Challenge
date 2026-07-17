#Recursion-is a technique where a function calls itself to solve a smaller version of the same problem
#structure of recursion-1:base case(stopping condition)
#                       -2:recursive call(fun call itself with smaller input)
#print 1 to N
def printnum(number):
    if number==0:
        return
    printnum(number-1)
    print(number)
printnum(5)
#print N to 1
def printnum(number):
    if number==0:
        return
    print(number)
    printnum(number-1)
    
printnum(5)
#factorial
def factorial(number):
    if number== 0:
        return 1
    return number*factorial(number-1)
    
print(factorial(5))
#sum of N natural numbers
def sumnatural(number):
   if number ==0:
      return 0
   return number+sumnatural(number-1)
print(sumnatural(5))
#printing hello n time
def hello(number):
   if number ==0:
      return
   print("Hello")
   hello(number-1)
hello(5)


   
