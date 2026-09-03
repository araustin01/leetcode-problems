class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1: # guard against
            return ""
        minimum_length = min([len(string) for string in strs]) # shortest string length from the list 
        output = "" # common prefix string
        for i in range(minimum_length):
            check = strs[0][i] # character to check against
            for string in strs[1:]: # check character against all other strings
                if string[i] != check:
                    # failed, return current common prefix string (early exit)
                    return output
            # passed all checks, append it
            output += check
        return output

        