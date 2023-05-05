def isValidSubsequence(array, sequence):
    for i in sequence:
        if(i in array):
            ind=array.index(i)
            array=array[ind+1:]
        else:
            
            return False
    return True
    # Write your code here.
    pass
