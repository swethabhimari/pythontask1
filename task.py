#1. Check if the list is already sorted or not. Ascending or descending

def checksorted(lst):
    ascending = True
    descending = True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            ascending = False
        if lst[i] < lst[i + 1]:
            descending = False
    if ascending:
        return "The list is sorted in ascending order."
    elif descending:
        return "The list is sorted in descending order."
    else:
        return "The list is not sorted."
lst = [5, 4, 3, 2, 1]
print(checksorted(lst))

#2.Missing number in a list. [1, 2, 3, 5,6,7,9, 8]
def missingnum(arr):
    n = len(arr) + 1  
    sum = (n * (n + 1)) // 2 
    actualsum = 0
    for i in arr:
        actualsum+=i
    return sum - actualsum
arr=[1,2,3,5,6,7,8,9]
print(missingnum(arr))

#3.Check if an array is a subset of another or not.
def issubset(arr1,arr2):
    for i in arr1:
        found = False
        for j in arr2:
            if i == j:
                found =True
                break
        if not found:
            return False
    return True
arr1=[1,2,3]
arr2=[1,2,3,4,5,6,7,8]
print(issubset(arr1,arr2))

#4. Check if a + b = target exists in a list
def sum_arr(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return True
        return False
arr=[1,2,3,4,5]
target=3
print(sum_arr(arr,target))
            