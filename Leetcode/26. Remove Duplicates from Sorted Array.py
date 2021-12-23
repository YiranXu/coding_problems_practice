#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Two pointer
        py,pm=1,1
        arrlen=len(nums)
        if arrlen==0:return 0
        while pm<arrlen:
            if nums[pm]!=nums[pm-1]:
                nums[py]=nums[pm]
                py+=1
            
            pm+=1
        return py   