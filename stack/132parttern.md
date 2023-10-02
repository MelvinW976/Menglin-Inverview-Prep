The numbers inside the stack are s2 and the number that popped out is the maximum s3. So the last thing to do is to maintain the order of the stack.

Have a stack, each time we store a new number, we first pop out all numbers that are smaller than that number. The numbers that are popped out becomes candidate for s3.
We keep track of the maximum of such s3 (which is always the most recently popped number from the stack).
Once we encounter any number smaller than s3, we know we found a valid sequence since s1 < s3 implies s1 < s2.
```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s3 = -math.inf
        # s3 > stack[-1] > n
        # 3    2           1 
        for n in nums[::-1]:
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False
```