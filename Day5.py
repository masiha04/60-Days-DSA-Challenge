#Advanced Array
#reversing a array
def reverse(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
arr=[1,2,3,4,5]
print(reverse(arr))
#right rotate by 1
def right_rotate(arr):
    temp1=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp1
    return arr

arr = [1, 2, 3, 4, 5]
print(right_rotate(arr))
#left rotation by k position
def reverse(arr,d):
    d = d % len(arr)  
    left=0
    right=d-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    left=d
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

    return arr
arr=[1,2,3,4,5]
print(reverse(arr,7))
#union two arrays
def union(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1

        elif arr2[j] < arr1[i]:
            result.append(arr2[j])
            j += 1

        else:
            result.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 5, 6]

print(union(arr1, arr2))
#intersection of two arrays
def intersection(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            i += 1

        elif arr2[j] < arr1[i]:
            j += 1

        else:
            result.append(arr1[i])
            i += 1
            j += 1

    return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 5, 6]

print(intersection(arr1, arr2))



