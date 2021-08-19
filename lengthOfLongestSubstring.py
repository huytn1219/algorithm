# Given a string s, find the length of the longest substring without repeating characters.
# Use sliding window algorithm to solve this problem.
# Time complexity: O(n) 
# Space complexity: O(n)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        charSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

s = "abcabcbb"
ob1 = Solution()
print(ob1.lengthOfLongestSubstring(s))