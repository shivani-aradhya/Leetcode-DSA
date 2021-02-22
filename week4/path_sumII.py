class Solution(object):
    def pathSum(self, root, sum):
        
        result = []
        if root:
            self.helper(root, [], result, sum)
        return result

    def helper(self, root, so_far, result, sum):
        if root.left is None and root.right is None and root.val == sum:
            so_far.append(root.val)
            result.append([x for x in so_far])
            so_far.pop()
        else:
            so_far.append(root.val)
            if root.left:
                self.helper(root.left, so_far, result, sum - root.val)
            if root.right:
                self.helper(root.right, so_far, result, sum - root.val)
            so_far.pop()
        return