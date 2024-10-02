class solution():
    def SmallestSecurityLevel(self, videoHash: str, encryptionKey: str) -> int:
        """
        swap ith item for these two string, found the smallest i so that vH < eK
        left to right, if same continue, if different, return i if ek >vH, else, already secured, return 0
        optimize: check if small at first to avoid furtur process
        """
        if videoHash < encryptionKey: return 0
        n = len(videoHash)
        for i in range(n):
            if videoHash[i] == encryptionKey[i]:
                continue
            elif videoHash[i] < encryptionKey[i]:
                return 0
            else:
                return i+1
        return -1




if __name__ == "__main__":
    s = solution()
    test1 = ['a', 'b']
    test2 = ['b', 'a']
    test3 = ['a', 'a']
    test4 = ['aaab', 'aacb']
    test5 = ['aacb', 'aabb']
    print(s.SmallestSecurityLevel(test3[0], test3[1]))
