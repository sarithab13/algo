import math
from typing import List
from itertools import combinations
from itertools import groupby
from collections import *
import calendar
from random import randrange
from random import choice
def maxOfAllSubArraysOfSizeK( arr,k) -> int:
    i=0
    j=0
    result=[]
    ls=[arr[0]]
    while(j<len(arr)):
        if(ls[0]<arr[j]):
            ls[0]=arr[j]
        if(j-i+1<k):
            j+=1
        if(j-i+1==k):
            result.append(ls[0])
            i+=1
            j+=1
    return result




print(maxOfAllSubArraysOfSizeK([1,3,-1,-3,5,3,6,7],3))

