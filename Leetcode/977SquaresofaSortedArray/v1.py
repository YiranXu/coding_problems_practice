class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #using sort
        #after square
        squares=list(map(lambda x:x**2,nums))
        return sorted(squares)