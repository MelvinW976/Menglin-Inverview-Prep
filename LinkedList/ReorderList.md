# find middle
slow, fast 
```python
slow = slow.next
fast = fast.next.next
```
# reverse list
需要一个pre node记录前一个node，也就是nhead
```python
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        
        while cur != None:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode
        return pre
```
# merge list
```python
# merge to sort
# 用一个dummy记录head，用一个
def merge(l, r):
            if not l or not r:
                return l if l else r
            dummy = p = ListNode(0)
            while l and r:
                if l.val < r.val:
                    p.next = l
                    l = l.next
                else:
                    p.next = r
                    r = r.next
                p = p.next
            p.next = l or r
            return dummy.next

# merge cross order
def merge(l, r):
    h1, h2 = l, r
    while h2:
        tmp = h1.next 
        h1.next = h2
        h1 = h2 
        h2 = tmp
    return l 
    
```

# Answer
```python
    def reorderList(self, head):
        #step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        node, pre = slow.next, None
        while node:
            n = node.next
            node.next = pre
            pre = node 
            node = n
        slow.next = None
        head1 = head
        head2 = pre
        # 1 2 3
        # 4 5 6
        # 1 4 2 3  
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
```

