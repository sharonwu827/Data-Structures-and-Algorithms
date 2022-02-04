
def partition(nums,left,right):
    # 初始化一个基准
    l,r=left,right
    pivot = nums[l]
    while l<r:
        # 从后往前查找，直到找到一个比pivot更小的数
        while l<r and nums[r]>=pivot:
            r-=1
        # 将更小的数放入左边
        nums[l] = nums[r]
        # 从前往后找，直到找到一个比pivot更大的数
        while l<r and nums[r] <= pivot:
            l+=1
        nums[r] = nums[l]  # 将更大的数放入右边
    # 循环结束，l与r相等
    nums[l] = pivot  # 待比较数据放入最终位置
    return l  # 返回待比较数据最终位置

def quicksort(nums,left,right):
    if left<right:
        index = partition(nums,left,right)
        quicksort(nums,left,index-1)
        quicksort(nums, index+1, right)


arr = [1,3,2,2,0]
quicksort(arr, 0, len(arr)-1)
print(arr)