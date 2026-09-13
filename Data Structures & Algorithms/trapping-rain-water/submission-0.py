class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : # meaning the input is 0
            return 0
        l , r = 0 , len(height) - 1
        leftMax , rightMax = height[l] , height[r]
        res = 0

        while l < r :  #before they meet each other 
            if leftMax < rightMax : # we r gonna shift by comparing lmax and rmax
                l += 1
                leftMax = max ( leftMax , height[l])
                res += leftMax - height[l]
            else:
                r -=1
                rightMax = max ( rightMax , height [r])
                res += rightMax - height[r]

        return res

        