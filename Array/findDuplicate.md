1. Because there are n+1 elements in arr and arr[i] in [1,n]
2. So, for a number mid, if we count the number <= mid, if count > mid, target number is [left, mid-1]
3. otherwise, [mid+1, right]. 
# 面对n个数，范围1-n这种可以考虑： count， 嵌套：nums[nums[i]], hashing

```python

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def count(mid):
            c = 0
            for n in nums:
                if n <= mid:
                    c += 1
            return c
        left, right = 1, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if count(mid) > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left
```