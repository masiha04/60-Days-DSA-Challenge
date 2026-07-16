#linear search
arr=[1,2,3,4,5]
target=7
for i in range(len(arr)):
    if arr[i]==target:
        print(i)
        break
else:
     print(-1)
#maximum number
arr1=[1,2,3,4,5]
max_value=arr1[0]
for i in range(1,len(arr1)):
    if arr1[i]>max_value:
        max_value=arr1[i]
print(max_value)
#minimum value
arr2=[1,2,3,4,5]
min_value=arr2[0]
for i in range(1,len(arr2)):
    if arr2[i]<min_value:
        min_value=arr2[i]
print(min_value)
#counting even number
arr3=[1,2,3,4,5]
count=0
for i in range(len(arr3)):
    if arr3[i]%2==0:
        count+=1
print(count)
#sum of all ements
arr4=[1,2,3,4,5]
total=0
for i in range(len(arr4)):
    total+=arr4[i]
print(total)
