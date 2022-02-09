# 返回某个值的问题

def binary_search(nums: List[int], target: int):
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            # 直接返回
            return mid
    return -1

# 返回左边界的问题

def left_bound(nums: List[int], target: int):
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            # 别返回，锁定左侧边界
            right = mid
    if left >= len(nums) or nums[left] != target:
        return -1
    return left

# 返回右边界的问题
def right_bound(nums: List[int], target: int):
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            # 别返回，锁定右侧边界
            left = mid + 1
    if right <0 or nums[right] != target:
        return -1
    return right




