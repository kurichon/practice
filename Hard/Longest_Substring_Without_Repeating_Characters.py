class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_set = set()
        left = 0
        longest_substring = 0
        for right in range(len(s)):
            while s[right] in substring_set: #check duplicate
                #move left pointer
                substring_set.remove(s[left]) #remove duplicate character while it exists
                left += 1
            #if no duplicate add to substring and update longest substring
            substring_set.add(s[right])
            longest_substring = max(longest_substring, right - left + 1)
        return longest_substring
