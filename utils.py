from random import uniform
import random
import time


def generateNewValue(lim1,lim2):
    l=[]
    for _ in range(lim2):
        l.append(-1)
    n=lim2
    while n>0:
        i=random.randint(lim1,lim2-1)
        while l[i]==-1:
            j=random.randint(lim1,lim2-1)

            if i!=j and j not in l:
                l[i]=j
                n=n-1
            if n==1 and i not in l and l[i]==-1:
                z=random.randint(lim1,lim2-1)
                l[i]=l[z]
                l[z]=i
                n=n-1
    return l