# 三个值，判断条件，值传递
O(N) 时间复杂度： 如果有比fmax大那老二接替旧老大， 老三接替老二。。。。

```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = second_max = third_max = float('-inf')
        unique_nums = set(nums)

        for num in unique_nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max:
                third_max = second_max
                second_max = num
            elif num > third_max:
                third_max = num

        return third_max if len(unique_nums) >= 3 else first_max

```