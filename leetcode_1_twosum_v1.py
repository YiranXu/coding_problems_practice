class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)): 
            p=i+1
            while nums[i]+nums[p]!=target:
                if i+p==len(nums)-1:
                    break
                p+=1
            if nums[i]+nums[p]==target:
                return [i,p]
        return None

if __name__ == "__main__":
    a=Solution()
    Solution().twoSum([6,5,7,8,9,3],10)
