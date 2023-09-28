We decode the string and N keeps the length of decoded string, until N >= K.
Then we go back from the decoding position.
If it's S[i] = d is a digit, then N = N / d before repeat and K = K % N is what we want.
If it's S[i] = c is a character, we return c if K == 0 or K == N

- 知道%号的使用，什么时候该用，什么时候
开始的时候
K : '-----'
N : '--'---'---'
N 变成了一个单位， K要找到正确的位置
K % N 
N : '--'
```python
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        """
        args: s, str, k, int
        loop s, if ch append, if digit, repeat
        return kth ch in tape
        """
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1

```