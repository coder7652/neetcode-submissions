class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
    # i is index and a is value and enumerate keeps track of the position of the value
    # i is more than 0 means this isnt the first value in input array
    #and for a - it means that it is the same value as before
    #in line 19sth - if and elif shifts, we dont have to worry abt tht and just think of shifting one pointer that is the left pointer
        for i, a in enumerate(nums):
            if i > 0 and a==nums[i-1]:
                continue
            l , r = i +1 , len(nums)-1 #r is the end of the list
            while l < r:
                threeSum = a + nums[l] + nums [r]
                if threeSum > 0 :
                    r -= 1
                elif threeSum < 0 :
                    l += 1
                else :
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r :  #l<r so that l pointer doest not cross the right pointer
                        l += 1 
        return res
        