class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for n in nums:
            digits=len(str(n))
            if digits%2==0: #even number of digits
                count+=1
        return count