class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 # coz we will be using sliding window
        res = 0
        #right pointer is gonnna go through every single character
        for r in range ( len (s)):  # menaing its a duplicate
            while s[r] in charSet :
                charSet.remove(s[l])
                l +=1
            charSet.add(s[r]) # add right most charcter to our set
            #now at this point we know there are no duplicates so add result variable
            res = max (res, r-l+1)
        return res

