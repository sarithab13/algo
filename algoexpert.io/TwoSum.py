def twoNumberSum(array, targetSum):
    res=[]
    listOfComplements=[]
    for i in range(0,len(array)):
        if(array[i] in listOfComplements):
            res.append(array[i])
            res.append(targetSum-array[i])
            return res
        else:
            listOfComplements.append(targetSum-array[i])
    return res
    
    # Write your code here.
    pass
