class Solution(object):
    def findMin(self, nums):

        if len(nums)==0:
            return -1            #BASE CASE
        if len(nums)==1:
            return nums[0]
        if nums[0]< nums[-1]:
            return nums[0]            #ALREADY IN SORTED ASCENDING ORDER

        left =0
        right= len(nums)-1

        while left<right:
            mid= (left+right)//2

            if nums[mid]>nums[right]:
                left = mid+1
            elif nums[mid] < nums[left]:
                right = mid
            else:
                right-=1                        #Right candidate would not be the pivot

        return nums[left]


"""class Solution(object):
    def findMin(self, nums):

        if len(nums)==0:
            return -1            #BASE CASE
        if len(nums)==1:
            return nums[0]
        if nums[0]< nums[-1]:
            return nums[0]            #ALREADY IN SORTED ASCENDING ORDER

        left =0
        right= len(nums)-1

        while left<right:
            while left <right and nums[left] == nums[left+1]:
                left +=1
            while left <right and nums[right] == nums[right-1]:
                right -=1
            mid= (left+right)//2

            if nums[mid]>nums[right]:
                left = mid+1
            
            else:
                right = mid                        

        return nums[left]"""