# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Using Nick White method in which we sort the list of strings and choose the prefix as the first string.
# Then iterate through the list from index 1. In each iteration, we will see if the string start with the prefix.
# If not, reduce the prefix until we have the common prefix.
# Time complexity is O(S) where S is the sum of all characters in all strings.
# Space complexity is O(1).
class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].startswith(prefix) == False:
                prefix = prefix[:len(prefix) - 1]
        return prefix

input_list = ["school","schedule","scotland"]
ob1 = Solution()
print(ob1.longestCommonPrefix(input_list))

