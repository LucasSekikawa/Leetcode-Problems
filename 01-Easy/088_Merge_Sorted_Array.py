class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m+n-1
        while j >= 0:
            if (i < 0) or (nums2[j] >= nums1[i]):
                nums1[k] = nums2[j]
                j = j - 1
            else:
                nums1[k] = nums1[i]
                i = i - 1
            k = k - 1
