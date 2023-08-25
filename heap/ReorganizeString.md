1. 
```python
class Solution:
    def reorganizeString(self, s: str) -> str:
        # altenatively place the most common char. 
        c = collections.Counter(s)
        ans = ""
        l = []
        for key , count in c.items():
            heapq.heappush(l, (-count, key))
        pre = (0, "")
        while len(l) > 0:
            cur = heappop(l) # pop and place the most comm
            ans += cur[1]
            if pre[0] < 0: # 如果上一个pop的还有数量，加进去
                heapq.heappush(l, pre)
            pre = (cur[0] + 1, cur[1]) # 当前的成为了pre 
        return ans if len(ans) == len(s) else ""
```