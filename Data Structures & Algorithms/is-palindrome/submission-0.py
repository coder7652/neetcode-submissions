class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s) -1  # left right pointer
# while the characters have not met or crossed each other 
        while l < r :       
            while l < r and not self.alphaNumeric(s[l]) :
                 l += 1 
            while l<r and not self.alphaNumeric(s[r]):
                r -= 1 
           
            if s[l].lower() != s[r].lower():
                return False 
            l += 1
            r -= 1

        return True

    def alphaNumeric (self,c):
        return ( ord('A')<= ord(c)<= ord('Z') or 
                 ord('a')<= ord(c)<= ord('z') or 
                 ord('0')<= ord(c)<= ord('9'))

                 # ord is for ASCII values 
