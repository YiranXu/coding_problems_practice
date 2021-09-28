import itertools
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([len(list(g)) for k,g in itertools.groupby(nums) if k==1],default=0)