"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:s

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


def func():
    prefix = ""
    strs = ["flower", "flow", "flight"]
    for i in range(len(strs[0])):
        for x in strs:
            if len(x) == i or strs[0][i] != x[i]:
                return prefix
        prefix += x[i]
    return prefix


print(func())
