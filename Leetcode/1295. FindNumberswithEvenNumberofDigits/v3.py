from math import floor,log10
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #using floor + log10 to calculate number of digits of a number
        return len(list(filter(lambda x:(floor(log10(x))+1)%2==0,nums)))