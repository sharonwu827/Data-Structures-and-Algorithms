

def bubble_sort(list_):
    for i in range(len(list_)-1,0,-1): # range(start, stop, step)
        for j in range(i):
            if list_[j]>list_[j+1]:
                list_[j],list_[j+1] = list_[j+1],list_[j]
    return list_

print(bubble_sort([1,2,0,3,6,4]))


def selection_sort(list_):
    for i in range(len(list_)):
        min_= i
        for j,v in range(i, len(list_)-1):
            if list_[i]<list_[j]:




def insert_sort(list_):
    length = len(list_)
    for i in range(1, length):
        pre = i - 1
        cur = list_[i]
        while pre>=0 and arr







