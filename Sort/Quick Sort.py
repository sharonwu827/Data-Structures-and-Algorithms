class Solution:
    def partition(self, nums, left, right):
        # 初始化一个待比较数据
        pivot = nums[left]
        while left < right:
            # 从后往前查找，直到找到一个比pivot更小的数
            while left < right and nums[right] >= pivot:
                right -= 1
            # 将更小的数放入左边
            nums[left] = nums[right]
            # 从前往后找，直到找到一个比pivot更大的数
            while left < right and nums[left] <= pivot:
                left += 1
            # 将更大的数放入右边
            nums[right] = nums[left]
        pivot = nums[left]  # 注意这里  不是nums[left] = pivot 而是要将pivot移到该在的index
        # 返回待比较数据最终位置
        return left

    def quickSort(self, nums, left, right):
        if left < right:
            index = self.partition(nums, left, right)
            self.quickSort(nums, left, index - 1)
            self.quickSort(nums, index + 1, right)
            return nums


