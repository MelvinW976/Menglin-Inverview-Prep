# 滑窗最大值
1. heap 里面存idx，如果最大值的idx不在window里面就一直pop

```python
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap, res = [], []
        for i in range(len(nums)):
            heappush(maxHeap, (-nums[i], i))
            if i >= k - 1:
                while maxHeap[0][1] <= i-k : #this is because the highest one is not in the window range
                    heappop(maxHeap)
                res.append(-maxHeap[0][0])
        return res

```