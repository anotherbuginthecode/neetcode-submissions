class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		nums = sorted(nums)
		ht = {}
		index = 0
		longest = 0
		

		if len(nums) == 0: return 0
		if len(nums) == 1: return 1

		ht[index] = nums[0]
		for i in range(1,len(nums)):
			if nums[i] - ht[len(ht)-1] == 0: 
				continue
			elif nums[i] - ht[len(ht)-1] == 1:
				index+=1
				ht[index] = nums[i]
			else:
				if len(ht) > longest:
					longest = len(ht)
				index = 0
				ht = {}
				ht[index] = nums[i]
		
		if longest > len(ht): 
			return longest
		else:
			return len(ht)

	