思路：
1. dp, dp[i] 0-i 最少extra char， 如果s[j:i] 能组成dict里的一个，

```python
class Solution:
    # dp[i] 0-i 最少extra，dp[i] = dp[j] 
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dict_set = set(dictionary)
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1 # 最关键的一步，不能放到jloop里，否则会覆盖min的步骤
            for j in range(i):
                if s[j:i] in dict_set:
                    dp[i] = min(dp[i], dp[j])
        return dp[-1]

```
