# importing "heapq" to implement heap queue
import heapq

test = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
# 将list x 转换成堆，原地，线性时间内
# python只支持小顶堆
heapq.heapify(test)

# # printing created heap
# print("The created heap is : ", end="")
# print(list(li))

# using heappush() to push elements into heap
# 添加和删除一个元素的时间复杂度都是O(logn)
heapq.heappush(test, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(test))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(test))


# 使用堆不仅仅可以存储单一值
# 默认将元组第一个值当做键来比较。如果第一个相同，继续比较第二个

h = [(1,2,3), (4,5,6), (2,1,3),(4,2,8)]
heapq.heapify(h) # 堆化（小顶堆）

heapq.heappop() # 弹出 (1,2,3)
heapq.heappop() # 弹出 (2,1,3)
heapq.heappop() # 弹出 (4,2,8)
heapq.heappop() # 弹出 (4,5,6)


# 手动实现

class Heap:
    def __init__(self, desc=False):
        """
        初始化，默认创建一个小顶堆
        """
        self.heap = []
        self.desc = desc

    @property
    def size(self):
        return len(self.heap)

    def top(self):
        if self.size:
            return self.heap[0]
        return None

    def push(self, item):
        """
        添加元素
        第一步，把元素加入到数组末尾
        第二步，把末尾元素向上调整
        """
        self.heap.append(item)
        self._sift_up(self.size - 1)

    def pop(self):
        """
        弹出堆顶
        第一步，记录堆顶元素的值
        第二步，交换堆顶元素与末尾元素
        第三步，删除数组末尾元素
        第四步，新的堆顶元素向下调整
        第五步，返回答案
        """
        item = self.heap[0]
        self._swap(0, self.size - 1)
        self.heap.pop()
        self._sift_down(0)
        return item

    def _smaller(self, lhs, rhs):
        return lhs > rhs if self.desc else lhs < rhs

    def _sift_up(self, index):
        """
        向上调整
        如果父节点和当前节点满足交换的关系
        （对于小顶堆是父节点元素更大，对于大顶堆是父节点更小），
        则持续将当前节点向上调整
        """
        while index:
            parent = (index - 1) // 2

            if self._smaller(self.heap[parent], self.heap[index]):
                break

            self._swap(parent, index)
            index = parent

    def _sift_down(self, index):
        """
        向下调整
        如果子节点和当前节点满足交换的关系
        （对于小顶堆是子节点元素更小，对于大顶堆是子节点更大），
        则持续将当前节点向下调整
        """
        # 若存在子节点
        while index * 2 + 1 < self.size:
            smallest = index
            left = index * 2 + 1
            right = index * 2 + 2

            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left

            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right

            if smallest == index:
                break

            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 初始化大顶堆
        heap = Heap(desc=True)
        for stone in stones:
            heap.push(stone)

        # 模拟
        while heap.size > 1:
            x, y = heap.pop(), heap.pop()
            if x != y:
                heap.push(x - y)
        if heap.size: return heap.heap[0]
        return 0



