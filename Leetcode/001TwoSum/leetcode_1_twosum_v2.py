class Solution:
    """
    Two-pass hash table
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            dic[nums[i]]=i #create the dictionary to store element and its index so we can quickly searches for index
        for i in range(len(nums)):
            comp=target-nums[i]
            #print(comp)
            if comp in dic.keys() and dic[comp]!=i: #note that there can be
                return [i,dic[comp]]
        return None