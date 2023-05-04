import math
from typing import List
from itertools import combinations
from itertools import groupby
from collections import *
import calendar
from random import randrange
from random import choice
def countOccurencesOfAnagrams( s: str,ptr:str) -> int:
    result=0
    k=len(ptr)
    d=dict()
    for i in ptr:
        if(i not in d):
            d[i]=1
        else:
            d[i]+=1
    count=len(d)
    i=0
    j=0
    while(j<len(s)):
        if(s[j] in d):
            d[s[j]]-=1
            if(d[s[j]]==0):
                count-=1
        if(j-i+1<k):
            j+=1
        elif(j-i+1==k):
            if(count==0):
                result+=1
            if(s[i] in d):
                d[s[i]]+=1
                if(d[s[i]]!=0):
                    count+=1
            i+=1
            j+=1
    return result











print(countOccurencesOfAnagrams("aabaabaa","aaba"))

