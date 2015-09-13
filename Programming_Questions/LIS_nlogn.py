def cel_index(arr, start , end , val):
    while start <= end:
        mid = (start + end)/2
        if arr[mid] >= val and (mid == 0  or arr[mid -1] < val):
            return mid
        elif arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
        
def LIS(nums, l):
    arr = []
    arr.append(nums[0])
    len = 1
    #print type(nums)
    for i in range(0, l):
        if nums[i] > arr[-1]:
            arr.append(nums[i])
            len += 1
        else:
            res = cel_index(arr, 0, len-1, nums[i])
            arr[res] = nums[i]
    return len


nums = [2, 8, 3, 4, 1, 56, -1, -5]
print LIS(nums, len(nums))
            
        
