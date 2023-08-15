# Perfect Pairs
1. min(|x-y|, |x+ y|) < min(|x|, |y|) and max(|x-y|, |x+y|) ≥ max(|x|, |y|) 的 solution space 四个象限是对称的，
所以只要求的第一象限的结果就行。
2. 转换 --> x > 0, y > 0, condition: 2x >= y 的perfect pairs.
3. 先abs再sort。binarysearch <= a * arr[i] 的 index，中间夹的所有的都可以是。

```python
def getNumberOfPairs(arr):
	for i in range(len(arr)):
		if arr[i] < 0:
			arr[i] = -arr[i]
	arr.sort()
	def binarysearch(arr, target):
		left, right = 0, len(arr) - 1
		while left <= right:
			mid = left + (right - left) // 2
			if arr[mid] > target:
				right = mid - 1
			elif arr[mid] < target:
				left = mid + 1
			else:
				return mid
		return right
	res = 0
	for i in range(len(arr)):
		index = binarysearch(arr, 2 * arr[i])
		# print(i, index)
		res += max(0, index - i)
	return res
arr = [2, 5, -3]
#[2 3 4]
print(getNumberOfPairs(arr))
```