class Solution(object):
    def partition(self, s):
        res=[]
        def helper(s, curr_list):
            if not s:
                res.append(curr_list)
            for i in range(len(s)):
               if s[:i+1]== s[:i+1][::-1]:
                   helper(s[i+1:], curr_list+ [s[:i+1]])
        helper(s,[])
        return res
