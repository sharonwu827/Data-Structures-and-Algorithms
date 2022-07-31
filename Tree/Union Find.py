https: // leetcode.cn / problems / number - of - provinces / solution / python - duo - tu - xiang - jie - bing - cha - ji - by - m - vjdr /


# 不带权并查集
class UnionFind:
    def __init__(self, n):
        self.parent = {} # O(N) space
        self.height = {}  # height for each set
        self.num_of_sets = 0

    def add(self, val):
        if val not in self.parent:
            self.parent[val] = val
            self.height[val] = 1
            self.num_of_sets += 1

    def find(self, val):
        '''
        get father of the val, return root of val
        '''
        if val != self.parent[val]:  # 路径压缩
            self.parent[val] = self.find(self.parent[val])
        return self.parent[val]

    def union(self, x, y, val):
        '''
        make x's father equal to y's father
        '''
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:  # 其实这里究竟把谁当做父节点一般是没有区别的
            self.parent[root_x] = root_y
            self.num_of_sets -= 1

    def union_compress(self, x, y): # worst case time complexity as O(Logn)
        '''
        union according to height of tree
        '''
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            # 合并时如果两棵树的高度不同 小的树挂到大的树上， 使树尽量平衡
            if self.height[root_x] < self.height[root_y]:
                self.parent[root_x] = root_y
                self.height[root_y] += self.height[root_x]
            else:
                self.parent[root_y] = root_x
                self.height[root_x] += self.height[root_y]
            self.num_of_sets -= 1

    def is_connected(self, x, y):
        """
        判断两节点是否相连
        """
        return self.find(x) == self.find(y)
