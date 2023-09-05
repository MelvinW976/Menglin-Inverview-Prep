# Problem
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
11101001
```python
def maxCon1(arr)
    ans = 0
    left, right = 0, 0
    n = len(arr)
    zero = 0
    while right < n:
        if arr[right] == 0:
            zero += 1
        while zero > 1:
            if arr[left] == 0:
                zero -= 1
            left += 1
        ans = max(ans, right - left + 1)
        right += 1
    return ans 
```