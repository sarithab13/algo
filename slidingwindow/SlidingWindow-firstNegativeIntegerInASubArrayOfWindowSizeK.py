import math
from typing import List
from itertools import combinations
from itertools import groupby
from collections import *
import calendar
from random import randrange
from random import choice
def firstNegativeIntegerInaSubArray( arr: List[int],k) -> int:
    ls=[]
    out=[]
    i,j=0,0
    while(j<len(arr)):
        if(arr[j]<0):
            ls.append(arr[j])
        if(j-i+1<k):
            j+=1
        elif(j-i+1==k):
            if(len(ls)==0):
                out.append(0)
            else:
                out.append(ls[0])
                if(arr[i]==ls[0]):
                    ls.pop(0)
            i+=1
            j+=1
    return out









print(firstNegativeIntegerInaSubArray([12,-1,-7,8,-15,30,13,28],3))

