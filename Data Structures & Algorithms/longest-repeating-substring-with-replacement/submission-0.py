class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hash map to count occurrences of each character
        res = 0

        l = 0

        for r in range (len(s)) :
            count[s[r]] = 1 + count.get(s[r],0)  #for the character at posiition r - increment the count of it ao 1 + watever the count currently was, if char doesnt exist them return default value of 0 

             # while the window is not valid that is no. of replacements we have to do is greater than np. of replacements allowed - so length of window minus cound of most frequent character
            while (r - l + 1) - max ( count.values()) > k :
                count[s[l]] -=1 # count of left char and decrement by 1
                l +=1
                 
            res = max (res, r-l+1) #r-1+1 is size of the window
        return res


        # or to the 7th line add maxF=0 so that in while loop we dotn have to use count.value to get max of entire hash map
        #then to the 10th line add maxF= max(maxF,count [s[r]]) coz maybe tht caharacter in count[s[r]] became the most freq char- this is a constant operation we r not scanning any list or something
        #replace the max(count.values()) in while loop to maxF


