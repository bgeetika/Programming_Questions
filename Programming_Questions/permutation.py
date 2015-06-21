nums = [1,2,3]


def swap(nums,a,b):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp
    

def permutation(nums, start, end):
    l = set()
    if start == end :
            yield list(nums)
    
    for i in xrange(start, end):
        if nums[i] not in  l :
            l.add(nums[i])
            swap(nums, start, i)
            x = permutation(nums, start+1, end)
            for y in x:
                yield y
            swap(nums,start, i)

for i in permutation(nums, 0, 3):
    print i

'''
def grange(start, end):
    i = start
    while i < end:
        yield i
        i += 1

for i in grange(10, 20):
    print i
    
'''
