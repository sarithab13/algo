import math
from typing import List
from itertools import combinations
from itertools import groupby
from collections import *
import calendar
from random import randrange
from random import choice
def maxsubarraysum( arr: List[int],k) -> int:
    mx=0
    i=0
    j=0
    sum=0
    while(j<len(arr)):
        sum+=arr[j]
        if(j-i+1<k):
            j+=1
        elif(j-i+1==k):
            mx=max(mx,sum)
            sum-=arr[i]
            i+=1
            j+=1
    return mx






print(maxsubarraysum([7,1,5,3,6,4],3))

