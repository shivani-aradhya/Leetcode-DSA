# Edge case is when two negative numbers make a max positive so we need to keep track of minimum product too.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result, prevmax, prevmin = nums[0]
        # COMPARISON STARTS FROM i=0 as we have already considered max as i=0

        for i in nums[1:]:
            currmax = max(i, prevmax * i, prevmin * i)  # LOCAL MAXIMUM
            currmin = min(i, prevmax * i, prevmin * i)  # LOCAL MINIMUM

            result = max(result, currmax)

            prevmax = currmax
            prevmin = currmin

        return result

