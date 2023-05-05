class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d=dict()
        i=0
        j=0
        mx=0
        sum=0
        while(j<len(nums)):
            sum+=nums[j]
            if(nums[j] in d):
                d[nums[j]]=d[nums[j]]+1
            else:
                d[nums[j]]=1
            if(len(d)>j-i+1):
                j+=1
            elif(len(d)==j-i+1):
                mx=max(sum,mx)
                j+=1
            elif(len(d)<j-i+1):
                while(len(d)<j-i+1):
                    d[nums[i]]=d[nums[i]]-1
                    sum=sum-nums[i]
                    if(d[nums[i]]==0):
                        d.pop(nums[i])
                    i+=1
                j+=1
        return mx
