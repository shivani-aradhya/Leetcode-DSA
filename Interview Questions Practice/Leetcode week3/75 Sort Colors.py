class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = len(nums) - 1

        while white <= blue:
            curr = nums[white]
            if curr == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif curr == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
