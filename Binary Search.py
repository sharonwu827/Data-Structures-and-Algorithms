
# 1.
# 寻找一个数（基本的二分搜索）
# 这个场景是最简单的，可能也是大家最熟悉的，即搜索一个数，如果存在，返回其索引，否则返回 -1
def binearySearch(nums, target):
    # 采用左闭右开区间[left,right)
    left = 0
    right = len(nums)
    while left<right:
        mid = left + (right - left) // 2
        # 当 nums[mid] 被检测之后，下一步的搜索区间应该去掉 mid 分割成两个区间，即 [left, mid) 或 [mid + 1, right)
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid  # 右开,真正右端点为mid-1
    return left  # 此算法结束时保证left = right,返回谁都一样

# 2
# 寻找左侧边界的二分搜索
def left_bound(nums, target):
    # 采用左闭右开区间[left,right)
    left = 0
    right = len(nums)
    if right == 0:
        return -1

    while left < right: # 终止的条件是 left == right
        mid = left + (right - left) // 2
        # 找到 target 时不要立即返回，而是缩小「搜索区间」的上界right，在区间 [left, mid) 中继续搜索，即不断向左收缩，达到锁定左侧边界的目的
        if nums[mid] == target:
            # 锁定左侧边界
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 检查left越界情况
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


# 3
# 寻找右侧边界的二分搜索

def right_bound(nums, target):
    # 采用左闭右开区间[left,right)
    left = 0
    right = len(nums)
    if right == 0:
        return -1
    while left < right:  # 终止的条件是 left == right
        mid = left + (right - left) // 2
        if nums[mid] == target:
            # 使得区间不断向右收缩，达到锁定右侧边界的目的
            left = mid+1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    if left ==0 or nums[left-1]!=target:
        return -1
    return right-1







