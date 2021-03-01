class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def con(root,dp,value):
            if root:
                if value+1 in dp:
                    dp[value+1].next=root
                dp[value+1]=root
                root.next=None
                con(root.left,dp,value+1)
                con(root.right,dp,value+1)
        con(root,{},0)
        return root