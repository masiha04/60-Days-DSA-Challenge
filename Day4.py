#Arrays
#finding the largest element
def largest(arr):
  max_value=arr[0]
  for i in range (len(arr)):
     if arr[i] >max_value:
       max_value=arr[i]
  return max_value
arr=[1,2,3,4,5]
print(largest(arr))
#finding the second largest elemnt
def second_largest(arr):
    max_value=float("-inf")
    second_value=float("-inf")
    for i in range(len(arr)):
        if arr[i]>max_value:
            second_value=max_value
            max_value=arr[i]
        elif arr[i]>second_value and arr[i]!=max_value:
            second_value=arr[i]
    return second_value
arr1=[1,2,3,4,5]
print(second_largest(arr1))
#checking sort
def is_sorted(arr2):
    for i in range(len(arr2)-1):
        if arr2[i]>arr2[i+1]:
            return False
    return True

arr2 = [1, 2, 3, 4, 5]
print(is_sorted(arr2))
#removing dublicates
def remove_duplicates(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i] !=arr[j]:
            i+=1
            arr[i]=arr[j]
    return arr[:i+1]
arr = [1, 1, 2, 2, 3, 4, 4]
print(remove_duplicates(arr))
#left rotation
def left_rotate(arr4):
    temp = arr4[0]

    for i in range(len(arr4)-1):
        arr4[i] = arr4[i+1]

    arr4[-1] = temp 

    return arr4


arr4= [1, 2, 3, 4, 5]
print(left_rotate(arr4))
#moving zeros
def move_zeros(arr):
    i = 0

    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1

    while i < len(arr):
        arr[i] = 0
        i += 1

    return arr
arr=[2,0,8,0,4,0]
print(move_zeros(arr))
