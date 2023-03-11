class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        l = []
        for j in range(1,len(s)):
            while j <= len(s):
                x = s[i:j:1]
                if x == x[::-1]:
                    l.append(x)
                i+=1
                j+=1
            i = 0
        print(l)


z = Solution()
z.longestPalindrome("sasgariir")