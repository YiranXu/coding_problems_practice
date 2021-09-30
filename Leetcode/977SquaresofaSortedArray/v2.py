class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Two pointer to compare absolute values
        n=len(nums)
        left=0
        right=n-1
        result=[0]*n
        index_result=-1
        while left<=right:
            
            if abs(nums[left])<=abs(nums[right]):
                result[index_result]=nums[right]**2
                right-=1
            else:
                result[index_result]=nums[left]**2
                left+=1
            index_result-=1 
        return result