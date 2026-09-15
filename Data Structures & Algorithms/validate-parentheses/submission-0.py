class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # we r using datastructure stack or in this case a python list
        #map close to open paranthesis - using hashmaps
        closeToOpen = {"]":"[" , ")" : "(" , "}" : "{" }

        for c in s :
            if c in closeToOpen :
                if stack and stack[-1] == closeToOpen[c] :
                    stack.pop()
                else :
                    return False
            else :
                stack.append(c)
        return True if not stack else False

