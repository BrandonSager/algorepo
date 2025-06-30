#binary search function
def bs(x, k):
    l = 0
    h = len(x) - 1
    m = (l + h) // 2

    while l <= h:

        if k == x[m]:
            return m
        elif k > x[m]:
            l = m + 1
            m = (l + h) // 2
        else:
            h = m - 1
            m = (l + h) // 2

    return "Not Found"

