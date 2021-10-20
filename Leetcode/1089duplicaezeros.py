class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        Two pass:
        1. check number of zeros to duplicate
        2. discard elements based on number of zeros to duplicate, then copy and move rightwards
        """
        
        numzero=0
        length=len(arr)
        for i in range(length):
            if i+numzero>length-1:
                break
            else:
                if arr[i]==0:
                    #edge case: the last digit to move is 0 ---> not duplicate
                    if i+numzero==length-1:
                        arr[length-1]=0  
                        length-=1
                        break
                    numzero+=1
        last=length-numzero-1
        for i in range(last,-1,-1):
            
            if arr[i-numzero]==0:
                arr[i]=0
                arr[i-1]=0
                numzero-=1
                i-=2
            else:
                arr[i]=arr[i-numzero]
                i-=1
            