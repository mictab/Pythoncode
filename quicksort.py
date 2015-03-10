#Simple recursive quicksort
#takes two lists

def quick(u, v):
  if u + 2 > v: return                #base case
  m = partition(u, v)
  quick(u, m)                         #recursively sorting left sublist
  quick(m + 1, v)                     #recursively sorting right sublist
