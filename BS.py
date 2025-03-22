def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low-high//2
    
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
             low=mid+1
        else:
            high=mid-1
    return -1

sorted_list=[1,2,4,5,6,7,8,9,10,11,12,14,16,17,18,19,22,26]
target=5
result=binary_search(sorted_list,target)
