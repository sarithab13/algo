import math
from typing import List
from itertools import combinations
from itertools import groupby
from collections import *
import calendar
from random import randrange
from random import choice
def LongestSubstringwithKUniqueCharacters(s: str,k:int) -> int:
    i=0
    j=0
    d=dict()
    mx=0
    while(j<len(s)):
        if(s[j] not in d):
            d[s[j]]=1
        else:
            d[s[j]]=d[s[j]]+1
        if(len(d)<k):
            j+=1
        elif(len(d)==k):
            mx=max(j-i+1,mx)
            j+=1
        else:
            while(len(d)>k):
                d[s[i]]-=1
                if(d[s[i]]==0):
                    d.pop(s[i])
                i+=1
            j+=1
    return mx











print(LongestSubstringwithKUniqueCharacters("aabacbebebe",3))

