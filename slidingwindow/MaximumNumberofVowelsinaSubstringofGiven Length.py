class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=0
        j=0
        mx=0
        vowels=['a','e','i','o','u']
        countofvowels=0
        while(j<len(s)):
            if(s[j] in vowels):
                countofvowels+=1
            if(j-i+1<k):
                j+=1
            elif(j-i+1==k):
                mx=max(mx,countofvowels)
                if(s[i] in vowels):
                    countofvowels-=1
                i+=1
                j+=1


        return mx