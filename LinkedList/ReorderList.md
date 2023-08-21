# find middle
slow, fast 
```python
slow = slow.next
fast = fast.next.next
```
# reverse list
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
        # head1, head2
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
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

