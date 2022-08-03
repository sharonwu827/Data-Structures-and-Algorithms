def merge_sort(arr):

    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2

    arrA = merge_sort(arr[:mid])
    arrB = merge_sort(arr[mid:])
    # 直到这里都是分割

    # 接下来才是比较合并
    arrA_index, arrB_index = 0, 0
    sorted_array = []
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            sorted_array.append(arrA[arrA_index])
            arrA_index += 1
        else:
            sorted_array.append(arrB[arrB_index])
            arrB_index += 1
    sorted_array += arrA[arrA_index:]
    sorted_array += arrB[arrB_index:]

    return sorted_array

arr = [ 12, 34, 54, 2, 3, -1, 0, -16]
print(merge_sort(arr))

# result
# [-16, -1, 0, 2, 3, 12, 34, 54]