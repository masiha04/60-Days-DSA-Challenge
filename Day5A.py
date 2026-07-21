#Array problems
#Missing number using sum()
def Missing(arr):
    n=len(arr)
    for i in range(len(arr)):
        expected_sum=n*(n+1)//2
        real_sum=sum(arr)
        missing_value=expected_sum-real_sum
    return missing_value
arr=[1,0,3]
print(Missing(arr))
#missing value using Xor
def miss_xor(arr):
    n=len(arr)
    xor=0
    for i in range(n+1):
        xor^=i
    for value in arr:
        xor^=value
        
    return xor
arr=[1,0,3]
print(miss_xor(arr))
#single number
def single(arr):
    xor=0
    for value in arr:
        xor^=value
        
    return xor
arr=[2,3,4,5,5,4,3]
print(single(arr)) 
#maximum consecutive ones
def consective(arr):
    count=0
    max_count=0
    for nums in arr:
        if nums==1:
            count+=1
            max_count=max(max_count,count)
        else:
            count=0
    return max_count
arr=[1,0,2,3,1,1,1,2,1]
print(consective(arr))
#maximum sub array sum(kadane's Algo)
def max_subarray(arr):
    current_sum=0
    max_sum=arr[0]
    for nums in arr:
        current_sum+=nums
        if current_sum>max_sum:
            max_sum=current_sum
        if current_sum<0:
            current_sum=0
    return max_sum
arr=[1,-2,3,-4,5,6,7]
print(max_subarray(arr))
#longest subarray
def longest_subarray(arr, k):
    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1

        if current_sum == k:
            max_len = max(max_len, right - left + 1)

    return max_len


arr = [1,2,1,1,1,3,2]
k = 4

print(longest_subarray(arr, k))
    

