class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxone=count=0
        for n in nums:
            if n==1: #increment the counter by 1, whenever you encounter a 1
                count+=1
            else: #find max and reset
                maxone=max(maxone,count)
                count=0
        maxone=max(maxone,count)
        return maxone