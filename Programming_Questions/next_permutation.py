import math 
nums = [1,3,2]


def swap(nums,a,b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    

                                                                                                                                                                               
def make_smaller_num(nums, start, end):
    def get_start_end():
        for x in range(start, end+1):
            for y in range(end, x, -1):
                if nums[y] < nums[x]:
                        swap(nums,x,y)
                        return x, y
    if start< end:
        start_end = get_start_end()
        if start_end is None:
            return
        start, _ = start_end
        make_smaller_num(nums,start,end)
                               
                                
    



def next_perm(nums):
     for i in range(len(nums)-2, -1, -1):
            least = None
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    if least is None or nums[j] < nums[least]:
                        least = j
            if least:
                swap(nums,least,i)
                make_smaller_num(nums, i+1, len(nums)-1)
                return
     nums.sort()


next_perm(nums)    
print nums    
