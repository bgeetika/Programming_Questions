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

#for i in permutation(nums, 0, 3):
 #   print i

    
def combination(nums):
    for x in __combination_internal(nums, 0, len(nums)):
          yield x
    yield {}
    
    
def __combination_internal(nums, start, end):
    if start == end - 1:
        yield [nums[start]]
    else:
        lis = __combination_internal(nums, start+1, end)
        for ele in lis:
            yield ele
            yield ele + [nums[start]]
        yield [nums[start]]
        
def combinations_k(nums, k, start, end):
    num_elems = end - start
    if num_elems < 0 or num_elems < k:
        return
    elif num_elems == k :
        yield nums[start:end]
    else:
        list1 = combinations_k(nums, k-1, start+1, end)
        for i in list1:
            yield i + [nums[start]]
        list2 = combinations_k(nums, k, start+1, end)
        for y in list2:
            yield y
    

    
def permutation_k(nums, k):
    for x in combinations_k(nums, k, 0, len(nums)):
         for y in permutation(x, 0, k):
                print y
        
    
    
    
    
k = 3    
permutation_k(nums,k)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
def grange(start, end):
    i = start
    while i < end:
        yield i
        i += 1

for i in grange(10, 20):
    print i
    
'''
