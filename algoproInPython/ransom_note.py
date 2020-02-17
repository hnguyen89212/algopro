"""
@Author:    Hai Nguyen
@Date:      Nov 6th, 2019
@Source:    AlgoPro
@Task:      Determine a binary tree is a valid binary search tree.
@Desc:      Given an arbitrary ransom note string and another string containing letters from all the magazines,
            write a function that will return true if the ransom note can be constructed from the magazines;
            otherwise, it will return false.
            Each letter in the magazine string can only be used once in your ransom note.
            You can assume that both strings contain only lowercase letters.
            For example:
            canConstruct("a", "b") -> false
            canConstruct("aa", "ab") -> false
            canConstruct("aa", "aab") -> true
"""

import collections


class Solution:
    def canConstruct(self, ransomNote, magazine):
        mag_dict = collections.defaultdict(int)
        for char in magazine:
            mag_dict[char] += 1
        for char in ransomNote:
            mag_dict[char] -= 1
            if (mag_dict[char]) < 0:
                return False
        return True


#Test
print(Solution().canConstruct('aa', 'aab'))  # true
print(Solution().canConstruct('abc', 'bbca'))  # true
print(Solution().canConstruct('abb', 'acb'))  # false
