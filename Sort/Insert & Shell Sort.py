
# 插入排序
#第i个元素左边的元素已经排序，将第i个元素与前边的已排序序列进行比较并交换, 遍历数组，完成排序
#时间复杂度：平均O(n^2), 最坏O(n^2), 最好O(n)
#稳定的排序算法

def insert_sort(numbers):
    # 外层循环控制遍历数组
    for i in range(len(numbers)):
        # 内层循环控制比较与交换
        for j in range(i):
            if numbser[j]>number[i]:
                numbser[j] , number[i] = numbser[i]>number[j]

## 插入排序升级版——希尔排序
# 等间隔取元素组成子序列进行排序，间隔逐渐变小，序列的长度逐渐曾长
# 如果所取的间隔互相不互质，那么小间隔的一部分序列则不起作用，效果变坏
#时间复杂度：平均O(n^1.3), 最坏O(n^2), 最好O(n)
#不稳定
def ShellSort(numbers):

    def insert(nums, d):
        """
        对子序列进行插入排序
        :param nums: 需要排序的序列
        :param d: 抽取子序列的间隔
        :return: 对子序列排序后的序列
        """
        for i in range(len(nums)//d):
            for j in range(i):
                back = i * d
                forward = j * d
                if nums[back] < nums[forward]:
                    nums[back], nums[forward] = nums[forward], nums[back]

        return nums

    d = len(numbers) //2
    while d >=1:
        numbers = insert(numbers, d)
        d = d //2






