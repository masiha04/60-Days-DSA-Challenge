#interveiw related recursive problems
#Fibonacci series
def fibonacci(number):
    if number == 0:
        return 0
    if number ==1:
        return 1
    return fibonacci(number-1)+ fibonacci(number-2)
print(fibonacci(5))
#reversing a string
def reverse_string(s):
    if s == "":
        return ""

    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))
#palindrome
def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

print(palindrome("madam"))   # True
print(palindrome("hello"))   # False
#printing array
def array(arr,index):
    if index==len(arr):
        return 
    print(arr[index])
    return array(arr, index + 1)
arr = [10, 20, 30, 40, 50]
array(arr, 0)
#maxvalue 
def maximum(arr, index, max_value):
    if index == len(arr):
        return max_value

    if arr[index] > max_value:
         max_value=arr[index]

    return maximum(arr,index+1,max_value)

arr = [4, 9, 2, 15, 7]
print(maximum(arr, 0, arr[0]))
