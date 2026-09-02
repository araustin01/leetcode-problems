class Solution(object):

    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        chars = list(s) # characters
        size = len(chars)

        for i in range(size):
            letter = chars[i] # current roman symbol
            value = Solution.symbols[letter] # value of current roman symbol
            
            sflag = 1   # sign flag
            if i < size - 1: # bound check
                next_letter = chars[i+1]
                if Solution.symbols[next_letter] > value: # is the next value greater? 
                    sflag = -1 # flip the sign
            total += sflag * value
        return total
            
        
        