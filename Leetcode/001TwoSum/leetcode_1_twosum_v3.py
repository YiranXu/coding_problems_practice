class Solution:
    """
    One-pass hash table
    While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. If it exists, we have found a solution and return immediately.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            comp=target-nums[i]
            
            
            if comp in dic.keys() and dic[comp]!=i: #note that there can be duplicates
                return [i,dic[comp]]
            else:
                dic[nums[i]]=i #create the dictionary to store element and its index so we can quickly searches for index
        return None