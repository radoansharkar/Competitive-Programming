class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        if len(s) == 1:
            ans = symbols[s[0]]
        else:
            ans = 0
            i = 0
            while i < len(s) - 1:
                if symbols[s[i]] < symbols[s[i + 1]]:
                    ans += symbols[s[i + 1]] - symbols[s[i]]
                    i += 1
                else:
                    ans += symbols[s[i]] 
                i += 1
            
            if len(s) > 1 and symbols[s[-2]] >= symbols[s[-1]]:
                ans += symbols[s[-1]]         
        
        return ans
    
