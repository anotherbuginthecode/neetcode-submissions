class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i,v in enumerate(nums):
            if i+1 >= len(nums): 
                return False
            if nums[i] == nums[i+1]: 
                return True
        return False