"""
@Author:    Hai Nguyen
@Date:      Nov 7th, 2019
@Source:    AlgoPro
@Task:      Determine a binary tree is a valid binary search tree.
@Desc:      
            
"""


class Solution:
    def threeSumBruteForce(self, nums):
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        res.add((nums[i], nums[j], nums[k]))
        return list(res)

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if (nums[i] == nums[i - 1] and i > 0):
                continue
            #two sum
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                if (nums[i] + nums[j] + nums[k] == 0):
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            #end of two sum
        return res


print(Solution().threeSumBruteForce([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

