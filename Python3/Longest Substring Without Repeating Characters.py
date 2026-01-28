class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        res = 0
        for i in range(n):
            # Optimization: If the remaining string is shorter than res, break
            if n - i <= res:
                break
            chars = set()
            for j in range(i, n):
                c = s[j]
                if c in chars:
                    break  # Break inner loop if duplicate found
                chars.add(c)
                res = max(res, j - i + 1)
        return res
            
