class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = self.create_hash_table(nums)
        for i, v in enumerate(nums):
            diff = target - v
            # check if diff exists in hash_table
            if diff in ht and ht[diff] != i:
                return [i, ht[diff]]
        return []

    def create_hash_table(self, nums: List[int]) -> List[int]:
        ht = {}
        for i, v in enumerate(nums):
            ht[v] = i
        return ht