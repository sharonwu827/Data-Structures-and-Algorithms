
# 首先选定一个轴心值p (如何选择？）
# 将数组中小于p的值移到数组左端，其他移动到数组右端 → partition
# 递归分别处理数组中p左右两边的子数组

# partition:
# 对于某个下标 j，nums[j] 已经排定，即 nums[j] 经过 partition（切分）操作以后会放置在它「最终应该放置的地方」。
# 而且：
## nums[left] 到 nums[j - 1] 中的所有元素<= nums[j]
## nums[j + 1] 到 nums[right] 中的所有元素都>= nums[j]


def partition(arr, left, right):
    pivot = arr[left] #初始化一个待比较数据
    while left<right:
        while left<right and arr[right]>=pivot:   # 从后往前查找，直到找到一个比pivot更小的数
            right-=1
        arr[left], arr[right] = arr[right], arr[left]
        while left<right and arr[left] <= pivot:  # 从前往后找，直到找到一个比pivot更大的数
            left += 1
        arr[left], arr[right] = arr[right], arr[left]
    return left  # nums[left] 到 arr[-1]是无序的 且>= nums[left], arr[0] 到nums[left]是无序的 且<= nums[left]


def quickSort(arr, left, right):
    if left<right:
        index = partition(arr, left, right)
        quickSort(arr, left, index - 1)
        quickSort(arr, index + 1, right)

arr = [4,2,6,5,3,9]
quickSort(arr, 0, len(arr)-1)
print(arr)


# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ji-yu-kuai-pai-de-suo-you-topkwen-ti-jia-ylsd/
# topk
# 将快速排序改成快速选择
# 寻找到一个位置，这个位置左边是k个比这个位置上的数更小的数，右边是n-k个比该位置上的数大的数
# 找到这个位置后停止迭代，完成了一次划分

def topk_split(arr, k, left, right):
    if left<right:
        index = partition(arr, left, right)
        if index==k:
            return
        elif index < k:
            topk_split(arr, k, index+1, right)
        elif index > k:
            topk_split(arr, k, left, index-1)

#获得前k小的数
def topk_smalls(arr, k):
    topk_split(arr, k, 0, len(arr)-1)
    return arr[k-1]

arr = [1,3,2,3,0,-19]
k = 2
print(topk_smalls(arr, k))
print(arr)

#获取第k小的数
def topk_small(arr, k):
    topk_split(arr, k, 0, len(nums)-1)
    return arr[k-1] #右边是开区间，需要-1

# 获得前k大的数
def topk_larges(nums, k):
    #parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
    topk_split(nums, len(nums)-k, 0, len(nums)-1) #把k换成len(nums)-k
    return nums[len(nums)-k:]

# 获得第k大的数
def topk_large(nums, k):
    #parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
    topk_split(nums, len(nums)-k, 0, len(nums)-1) #把k换成len(nums)-k
    return nums[len(nums)-k]

# 只排序前k个小的数
#获得前k小的数O(n)，进行快排O(klogk)
def topk_sort_left(nums, k):
    topk_split(nums, k, 0, len(nums)-1)
    topk = nums[:k]
    quicksort(topk, 0, len(topk)-1)
    return topk+nums[k:] #只排序前k个数字

# arr = [0,0,1,3,4,5,0,7,6,7]
# k = 4
# topk_sort_left(arr, k)

#只排序后k个大的数
#获得前n-k小的数O(n)，进行快排O(klogk)
def topk_sort_right(nums, k):
    topk_split(nums, len(nums)-k, 0, len(nums)-1)
    topk = nums[len(nums)-k:]
    quicksort(topk, 0, len(topk)-1)
    return nums[:len(nums)-k]+topk #只排序后k个数字

arr = [0,0,1,3,4,5,0,-7,6,7]
k = 4
print(topk_sort_right(arr, k))
