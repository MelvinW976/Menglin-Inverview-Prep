# 可以用很多次.思路要清楚。dp[n] 可以组合成n有多少种。
# In the example given, we can actually find the # of combinations of 4 with the # of combinations of 3(4 - 1), 2(4- 2) and 1(4 - 3). As a result, comb[4] = comb[4-1] + comb[4-2] + comb[4-3] = comb[3] + comb[2] + comb[1]
   
```python
class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for j in range(n):
                if i >= nums[j]:
                    dp[i] += dp[i-nums[j]]
        return dp[-1]

```

# another similar problem need to attention:
# 找零钱II， 给一个target，多少种凑出零钱的方法，这样就不用在意顺序， 这俩的区别就是for循环谁先的问题
# create use an outer loop of coins so that a combination once used cannot be used again.

```python
class Solution:
    # dp[5] = 
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for i in coins:
            for j in range(1, amount+1):
                if j >= i:
                    dp[j] += dp[j-i]
        return dp[amount]
```