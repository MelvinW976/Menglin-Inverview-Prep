双指针，让j负责填最后返回的格子，i去扫描，因为i总要比j快，所以不存在交叉的问题

```python

    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
```