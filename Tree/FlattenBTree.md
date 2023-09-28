
If we traverse the flattened tree in the reverse way, we would notice that [6->5->4->3->2->1] is in (right, left, root) order of the original tree. So the reverse order after flattening is post order traversal in (right, left, root) order like [6->5->4->3->2->1].
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
