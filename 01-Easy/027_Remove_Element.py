class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i <= (len(nums)-1):
            if nums[i] == val:
                nums.pop(i)
                i = i - 1
            i = i + 1
        return len(nums)
