```python
1. 两个str可不可子串穿插成第三个str
2. dp[i][j], s1前i 和 s2前j 能否构成 s3 i+j
3. 初始化，s2 是空，如果s1[i] != s3[i], 则后面的dp都是false
4. s1 = aabcc
   s2 = dbbca
   s3 = aadbbcbcac
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp[i][j], s1前i 和 s2前j 能否构成 s3 i+j
        l1, l2, l3 = len(s1) + 1, len(s2) + 1, len(s3) + 1
        if len(s1) + len(s2) != len(s3): return False
        dp = [[True] * l2 for _ in range(l1)]
        for i in range(1, l1):# 
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, l2):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]    
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]
```