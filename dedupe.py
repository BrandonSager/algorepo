def dedupe(nums):    
    ht = {}
    for i in nums:
        if i not in ht:
            ht[i] = 1
        else:
            ht[1] += 1
    return list(ht.keys())


print(dedupe([1,1,1,2,4,7,7,9,4,32]))
