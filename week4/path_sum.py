class Solution:
    def hasPathSum(self, r: TreeNode, t: int) -> bool:
        c=0
        def mini(r,c):
            if r==None:
                return False
            if r.left==None and r.right==None:
                c+=r.val
                if c==t:
                    return True
                else:
                    return False
            return mini(r.left,c+r.val) or mini(r.right,c+r.val)
        if(r==None):
            return False
        if(mini(r,c)):
            return True
        return False