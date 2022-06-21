def maxHepify(nums, n, i):
    '''
    To heapify subtree rooted at index i
    :param nums: array
    :param n: size of heap
    :param i: subtree rooted at index i, which we are trying to heapify
    '''
    largest = i  # Initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2
    # See if left child of root exists and is greater than root
    if l < n and nums[largest] < nums[l]:
        largest = l
    # See if right child of root exists and is greater than root
    if r < n and nums[largest] < nums[r]:
        largest = r
    # Change root, if needed
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]  # swap
        # Heapify the root.
        maxHepify(nums, n, largest)


def heapSort(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        maxHepify(arr, n, i)
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        maxHepify(arr, i, 0)

# Driver code
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i],end=" ")