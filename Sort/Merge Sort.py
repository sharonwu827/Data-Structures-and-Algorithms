def mergesort(self,seq):
		"""归并排序"""
		if len(seq) <= 1:
			return seq
		mid = len(seq) // 2  # 将列表分成更小的两个列表

		# 分别对左右两个列表进行处理，分别返回两个排序好的列表
		left = self.mergesort(seq[:mid])
		right = self.mergesort(seq[mid:])

		# 对排序好的两个列表合并，产生一个新的排序好的列表
		return self.merge(left, right)

	def merge(self, left, right):
		"""合并两个已排序好的列表，产生一个新的已排序好的列表"""
		result = []  # 新的已排序好的列表
		i = 0  # 下标
		j = 0
		# 对两个列表中的元素 两两对比。
		# 将最小的元素，放到result中，并对当前列表下标加1
		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
		result += left[i:]
		result += right[j:]
		return result

arr = [ 12, 34, 54, 2, 3, -1, 0, -16]
print(mergesort(arr))

# result
# [-16, -1, 0, 2, 3, 12, 34, 54]