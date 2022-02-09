#冒泡排序

#利用双层循环，外层循环控制比较的次数，内层循环控制交换归位数据
#时间复杂度：平均O(n^2), 最坏O(n^2), 最好O(n)
#稳定的排序算法

def bubble_sort(list_):
    for i in range(len(list_)-1,0,-1): # range(start, stop, step)
        for j in range(i):
            if list_[j]>list_[j+1]:
                list_[j],list_[j+1] = list_[j+1],list_[j]
    return list_

print(bubble_sort([1,2,0,3,6,4]))


