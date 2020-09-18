from typing import List

class Solution:
    def TwoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target: return[i,j]

    def ListTwoSum(self, nums: List[int], target: int) -> List[int]:
        #list for storing complements
        comps = []

        #go through list
        for i in range(len(nums)):
            #check if complement already exists
            try:
                return [comps.index(nums[i]), i]
            except ValueError:
                comps.append(target - nums[i])

    def DictTwoSum(self, nums: List[int], target: int) -> List[int]:
        #list for storing complements
        comps = {}
        #store the first complement
        comps[target - nums[0]] = 0
        #go through list
        for i in range(1,len(nums)):
            #check if complement already exists
            if nums[i] in comps:
                return [comps[nums[i]], i]
            else:
                comps[target - nums[i]] = i



Sean = Solution()
print(Sean.TwoSum([0,2,2,5],4))
print(Sean.ListTwoSum([0,2,2,5],4))
print(Sean.DictTwoSum([0,2,2,5],4))
print(Sean.DictTwoSum([2,7,11,15],9))