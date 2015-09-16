nums = [-7,-5,-1,0,2,4,9,10]


def find_index(nums, start, end):
    while start <= end:
        mid = (start + end)/2
        if nums[mid] < 0 and (mid == len(nums) -1 or nums[mid + 1] >= 0):
            return mid
        elif nums[mid] < 0:
            start = mid + 1
        else:
            end = mid - 1
    return None


def do_square(lis):
    for i in range(0, len(lis)):
        lis[i] = lis[i]*lis[i]
    return lis

def merge_lists(nums, index):
    lis = []
    i = index
    j = index + 1
    for x in range(0, index + 1):
        nums[x] = abs(nums[x])

    print nums
    
    while i >= 0 and j <= len(nums)-1:
        if nums[i] <  nums[j]:
            lis.append(nums[i])
            i -= 1
        else:
            lis.append(nums[j])
            j += 1
    while i >= 0:
        lis.append(nums[i])
        i -= 1
    while j <= len(nums)-1:
        lis.append(nums[j])
        j += 1
    print lis
    return lis
            
            
            
def sorted_squares(nums):
    print nums
    res = find_index(nums, 0, len(nums))
    if res is None or res == len(nums) - 1:
        return do_square(nums)
    else:
        lis = merge_lists(nums, res)
        return do_square(lis)
    
    
print sorted_squares(nums)
