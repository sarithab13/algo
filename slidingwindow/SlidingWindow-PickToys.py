import math
from typing import List
from itertools import combinations
from itertools import groupby
from collections import *
import calendar
from random import randrange
from random import choice
def pickToys(s: str) -> int:
    i=0
    j=0
    mx=0
    d=dict()
    while(j<len(s)):
        if(s[j] in d):
            d[s[j]]=d[s[j]]+1
        else:
            d[s[j]]=1
        if(len(d)<2):
            j+=1
        elif(len(d)==2):
            mx=max(mx,j-i+1)
            j+=1
        elif(len(d)>2):
            while(len(d)>2):
                d[s[i]]=d[s[i]]-1
                if(d[s[i]]==0):
                    d.pop(s[i])
                i+=1
            j+=1





    return mx






print(pickToys("abaccab"))

