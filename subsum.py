#Function that finds the greatest sub-sum in a given list

def gsum(alist):
    best = current = 0
    for i in alist:
        current = max(current + i, 0)
        best = max(best, current)
    return best
