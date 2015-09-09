import math
import random



def swap(nums, i , j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    
def find_index(nums, n):
    return int(math.floor(len(nums)*n))
    
def percent(nums, n): 
    #give n , it will return index having more than n percentile.  
    index = find_index(nums, n)
    if index >= len(nums):
        return None
    start = 0
    end = len(nums) - 1
    x = 0
    while start <= end :
        parti = partion(nums, start, end)
        if parti is None:
            return None
        if parti == index :
            return nums[parti]
        elif parti > index :
            end = parti - 1
        else:
            start = parti + 1
            
def percent1(nums, n): 
    #give n , it will return index having more than n percentile.  
    index = find_index(nums, n)
    if index >= len(nums):
        return None
    start = 0
    end = len(nums) - 1
    x = 0
    while start <= end :
        parti1, parti2 = partion1(nums, start, end)
        if parti1 <= index and parti2 >= index:
            if parti2 == index:
                return nums[parti2]
            else:
                return nums[parti1]
        elif parti1 > index :
            end = parti1 - 1
        else:
            start = parti2 + 1

def partion(nums, start, end):
    if start > end:
        return None
    x = random.randint(start,end)
    swap(nums, x, end)
    pivot = nums[end]
    i =  start - 1
    while start < end:
        move_left = False
        if nums[start] == pivot:
            probab = random.randint(0,1)
            if probab == 1:
                move_left = True
        if move_left or nums[start] < pivot:
            i = i  + 1
            swap(nums, i , start)
        start = start + 1
    i = i + 1
    swap(nums, end, i)
    return i

def partion1(nums, start, end):
    start_bck = start
    if start > end:
        return None
    x = random.randint(start,end)
    swap(nums, x, end)
    pivot = nums[end]
    i =  start - 1
    while start < end:
        if  nums[start] <= pivot:
            i = i  + 1
            swap(nums, i , start)
        start = start + 1
    i = i + 1
    swap(nums, end, i)
    
    j = start_bck - 1
    for x in range(start_bck,i):
        if nums[x] != pivot:
            j += 1
            swap(nums, x , j)
    return j, i
       
nums = [1,2,3,4,5,6,7,8,9,10]
print percent1(nums, 0.4)
