
# 记住binarysearch最关键是mid相对于target的位置
[4, 5, 6, 7, 1, 2, 3]
      left  | right
- 可以分成两部分呢
- nums[mid] > nums[left] 说明mid肯定在left，否则肯定在right
- 在left的话，如果target在nums[left]和nums[mid]中间说明target 一定在mid左边，否则在mid右边
```python
class Solution:
    def search(self, nums: List[int], target) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left)// 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1   

```