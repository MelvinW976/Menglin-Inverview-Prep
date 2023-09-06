# Problem
split a singly-linked list into kkk consecutive parts. Each part should have nearly equal length, differing at most by 1. The parts should be in the same order as they appear in the original list, and parts occurring earlier should have a size greater than or equal to parts occurring later.

# cut + (remain > 0)

# dummy 来作为curr的前一个node，更好操作

```python
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def size(head):
            if not head: return 0
            return size(head.next) + 1
        size = size(head)
        ans = []
        curr = head
        cut, remain = divmod(size, k)
        for _ in range(k):
            dummy = ListNode()
            phead = dummy
            for _ in range(cut + (remain > 0)):
                dummy.next = curr
                curr = curr.next
                dummy = dummy.next #！！！ 这三行就是始终保持dummy在curr的前一个node，到时候好操作None
            if remain > 0:
                remain -= 1
            ans.append(phead.next)
            if dummy: dummy.next = None 
        return ans 
                    
```