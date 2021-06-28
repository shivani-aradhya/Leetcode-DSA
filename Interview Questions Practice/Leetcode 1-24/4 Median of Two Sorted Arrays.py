class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A= nums1
        B = nums2
        if len(A) > len(B):
            A, B = B, A
        low = 0
        high = len(A)
        total = len(A) + len(B)

        while low <= high:
            mid = (low + high) // 2
            aleft = mid
            bleft = ((total + 1) // 2) - aleft

            aleftmax = (A[aleft - 1] if aleft > 0 else float("-inf"))
            bleftmax = (B[bleft - 1] if bleft > 0 else float("-inf"))
            arightmin = (A[aleft] if aleft != len(A) else float("inf"))
            brightmin = (B[bleft] if bleft != len(B) else float("inf"))

            if aleftmax <= brightmin and bleftmax <= arightmin:
                if total % 2 == 0:
                    median = (max(aleftmax, bleftmax) + min(arightmin, brightmin)) / 2
                    return median
                else:
                    median = max(aleftmax, bleftmax)
                    return median

            elif aleftmax > brightmin:
                high = aleft - 1
            elif bleftmax > arightmin:
                low = aleft + 1