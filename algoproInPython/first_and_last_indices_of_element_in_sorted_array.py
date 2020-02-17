"""
@Author:    Hai Nguyen
@Date:      Nov 8th, 2019
@Source:    AlgoPro
@Task:      Find the first and last indices of an integer (target) in a sorted array.
@Desc:      For example, given a sorted array [1, 3, 4, 5, 5, 7, 10] and target = 5
            The algorithm returns an array [4, 5] since the first appearance of 5 is at index 4. Etc.
"""


class Solution:
    def getRange(self, arr, target):
        first = self.binarySearchRecursive(arr, 0, len(arr) - 1, target, True)
        last = self.binarySearchRecursive(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binarySearchRecursive(self, arr, low, high, target, findFirst):
        # Simple check for validity
        if (high < low):
            return -1
        # determine the middle index
        mid = low + (high - low) // 2
        # find index of first appearance
        if (findFirst):
            """ 
            Anchor:
                1/ If middle index is 0 and element at that index is equal to target
                2/ If the element to the left (at index mid - 1) is less than target and element at that index (mid) is equal to target
                Then we have the first appearance of target.
            """
            if (mid == 0 or arr[mid - 1] < target) and arr[mid] == target:
                return mid
            """
            Otherwise, if target is greater than the element at that index
            Recursively call function, pass in the low index as (mid + 1)
            The other way around is likewise: replace high index as (mid - 1)
            """
            if (target > arr[mid]):
                return self.binarySearchRecursive(arr, mid + 1, high, target, findFirst)
            else:
                return self.binarySearchRecursive(arr, low, mid - 1, target, findFirst)
        #find index of last appearance
        else:
            if (mid == len(arr) - 1 or arr[mid + 1] > target) and arr[mid] == target:
                return mid
            if (target < arr[mid]):
                return self.binarySearchRecursive(arr, low, mid - 1, target, findFirst)
            else:
                return self.binarySearchRecursive(arr, mid + 1, high, target, findFirst)


#Test
arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
print(Solution().getRange(arr, 15))  # [9, 9]
print(Solution().getRange(arr, 9))  # [6, 8]
