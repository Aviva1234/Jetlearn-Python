def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left<=right:
        mid = (left+right) // 2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            right = mid-1
        else:
            left = mid+1
    
    return -1

numbers = [10,20,30,40,50,60,70,80,90]

print(binarySearch(numbers, 40))