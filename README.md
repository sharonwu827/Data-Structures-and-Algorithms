# Data Structures and Algorithms

## Algorithms TLDR

### Binary Search

```python
# 1.
# 寻找一个数（基本的二分搜索）
# 这个场景是最简单的，即搜索一个数，如果存在，返回其索引，否则返回 -1
def binearySearch(nums, target):
    # 采用左闭右开区间[left,right)
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        # 当 nums[mid] 被检测之后，下一步的搜索区间应该去掉 mid 分割成两个区间，即 [left, mid) 或 [mid + 1, right)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        elif nums[mid] == target:
            return mid  # 右开,真正右端点为mid-1
    return left  # 此算法结束时保证left = right,返回谁都一样


# 2
# 寻找左侧边界的二分搜索
# 左侧边界定义为 数字最左边的边界或者第一个大于该数字
def left_bound(nums, target):
    # 采用左闭右开区间[left,right)
    left = 0
    right = len(nums)
    if right == 0:
        return -1

    while left < right:  # 终止的条件是 left == right
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
    # if left >= len(nums) or nums[left] != target:
    #     return -1
    return left


# 3
# 寻找右侧边界的二分搜索
# 右侧边界定义为 x ≥ target 的第一个元素

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
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # if left ==0 or nums[left-1]!=target:
    #     return -1
    return right - 1
```

### Sliding Window

```python
class Solution:
    def problemName(self, s: str) -> int:
        # Step 1: 定义需要维护的变量们 (对于滑动窗口类题目，这些变量通常是最小长度，最大长度，或者哈希表)
        x, y = ..., ...

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3: 更新需要维护的变量, 有的变量需要一个if语句来维护 (比如最大最小长度)
            x = new_x
            if condition:
                y = new_y

            '''
            ------------- 下面是两种情况，读者请根据题意二选1 -------------
            '''
            # Step 4 - 情况1
            # 如果题目的窗口长度固定：用一个if语句判断一下当前窗口长度是否达到了限定长度 
            # 如果达到了，窗口左指针前移一个单位，从而保证下一次右指针右移时，窗口长度保持不变, 
            # 左指针移动之前, 先更新Step 1定义的(部分或所有)维护变量 
            if 窗口长度达到了限定长度:
            # 更新 (部分或所有) 维护变量 
            # 窗口左指针前移一个单位保证下一次右指针右移时窗口长度保持不变

            # Step 4 - 情况2
            # 如果题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 如果当前窗口不合法时, 用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 在左指针移动之前更新Step 1定义的(部分或所有)维护变量 
            while 不合法:
        # 更新  (部分或所有) 维护变量 
        # 不断移动窗口左指针直到窗口再次合法

        # Step 5: 返回答案
        return ...
```
### DP
```python
# Matrix, rows = i, colomns = j 
[[0 for _ in range(cols)] for _ in range(rows)]
[[False] * j for _ in range(i)]
```
### QuickSort
```python
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
        nums[left] = pivot  # 注意这里要将pivot移到该在的index
        # 返回待比较数据最终位置
        return left

    def quickSort(self, nums, left, right):
        if left < right:
            index = self.partition(nums, left, right)
            self.quickSort(nums, left, index - 1) #Sorts the elements to the left of pivot
            self.quickSort(nums, index + 1, right) #sorts the elements to the right of pivot
            return nums
```



## Big-O complexity Chart

- O(1): constant - no loops
- O(Log N): Logarithmic, usually searching algorithms have log n if they are sorted (Binary Search)
- O(n): Linear, for loops, while loops through n items
- O(n log(n)): Log Linear, usually sorting operations
- O(n^2): Quadratic, every element in a collection needs to be compared to ever other element. Two nested loops
- O(2^n): Exponential, recursive algorithms that solves a problem of size N
- O(n!): Factorial, you are adding a loop for every element
- Iterating through half a collection is still O(n)
- Two separate collections: O(a * b)

