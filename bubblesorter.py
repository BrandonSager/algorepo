x=[5,2,8,1,6,3,9,0,1,4]

def bubblesorter(x):
    changes = 0
    for i in range(len(x)-1):
        
        if x[i] < x[i+1]:
            t = x[i]
            x[i] = x[i+1]
            x[i+1] = t
            changes += 1
    if changes > 0:
        return sorter(x)
    
    return x
        
print(sorter(x))


