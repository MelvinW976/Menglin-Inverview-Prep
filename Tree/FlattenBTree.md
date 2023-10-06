
1. If we traverse the flattened tree in the reverse way, we would notice that [6->5->4->3->2->1] is in (right, left, root) order of the original tree. So the reverse order after flattening is post order traversal in (right, left, root) order like [6->5->4->3->2->1].
# and then set each node's right pointer as the previous one


```python
class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        [1,2,3,4,5,6]
        flatten left -> left
        flatten right -> right
        root.right = left 

        """
        if not root: return 
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
```
2. Flattern a linkedList with a child pointer:
# reflection: 找到有child的node，再从child一直next找到child的tail， 再插入node里，注意操作完要把node的chlid给None

```python
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        node = head
        while node:
            if not node.child:
                node = node.next
                continue
            tail = node.child
            while tail.next:
                tail = tail.next
            tail.next = node.next
            if node.next: node.next.prev = tail
            node.next = node.child
            node.child.prev = node
            node.child = None 
        return head
```