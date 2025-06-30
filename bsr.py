#binarysearchrecursivefunction

def bsr(x,k):

    l =0
    h = len(x) - 1

    def helper(l,h):

        if l > h:
            return "not found"

        m = (l + h) // 2

        if k == x[m]:
            return m
    
        if k < x[m]:
            return helper(l,h = m - 1)  

        else:
            return helper(l = m + 1,h = h)

    return helper(l,h)
