x = [4, 10, 3, 5, 1, 2, 7] #len 7
#0, 1,  2, 3 ,4, 5, 6

# [10, 4, 7, 5, 1, 2, 3]

def heapify(x):
    
    xlen = len(x)
    def pcomp(x,xlen):
    for pix in range(xlen//2 - 1,-1,-1):
        greatestix = pix
        cix1 = (pix * 2)+1
        cix2 = (pix * 2)+2
        
        if (cix2<=xlen) and (x[cix2] > x[greatestix]):
            greatestix = cix2

        if (cix1<=xlen) and (x[cix1] > x[greatestix]):
            greatestix = cix1
        
        if pix != greatestix:
            x[pix], x[greatestix] = x[greatestix], x[pix]
    return x
        

print(heapify(x))



