class solution:
    def CommonDivisors(self, s1: str, s2: str) -> int:
        """
        for s1, s2, we need to find all number of the common divisors.
        求最大公因数：辗转相除法
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        求最小公倍数：两数相乘 // 最大公因数
        
        """
        """res = 0
        divSet = set()
        n1, n2 = len(s1), len(s2)
        for i in range(n1):
            if n1 % (i+1) != 0:
                continue
            div = s1[:i+1]
            if div * (n1 // (i+1)) == s1:
                divSet.add(div)
        for i in range(n2):
            if n2 % (i+1) != 0:
                continue
            div = s2[:i+1]
            if div * (n2 // (i+1)) == s2 and div in divSet:
                res += 1
        return res

        """
        if s1 + s2 != s2 + s1:
            return 0
        if len(s1) > len(s2):
            a, b = len(s1), len(s2)
        else:
            a, b = len(s2), len(s1)
        while b != 0:
            a, b = b, a % b
        res = 0
        for i in range(a):
            if a % (i+1) == 0:
                candidate = s1[:i+1]
                if candidate * (a // (i+1)) == s1[:a]:
                    res += 1
        return res







    
if __name__ == '__main__':
    s = solution()
    test1 = ['aaaaaa', 'aaaaaaaaa']
    print(s.CommonDivisors(test1[0], test1[1]))


