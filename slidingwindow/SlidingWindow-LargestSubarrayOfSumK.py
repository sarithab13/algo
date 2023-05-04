import math
from typing import List
from itertools import combinations
from itertools import groupby
from collections import *
import calendar
from random import randrange
from random import choice
def LongestSubarrayOfSumk( arr,k) -> int:
    i=0
    j=0
    sum=0
    mx=0
    while(j<len(arr)):
        sum+=arr[j]
        if(sum<k):
            j+=1
        elif(sum==k):
            if(j-i+1>mx):
                mx=j-i+1
            j+=1
        else:
            while(sum>k):
                sum=sum-arr[i]
                i+=1
            j+=1
    return mx







print(LongestSubarrayOfSumk([4,1,1,1,1,1,2,3,5],5))

