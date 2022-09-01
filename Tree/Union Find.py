class UnionFind:
    def __init__(self):
        self.parent = {}
        self.height = {}  # height for each set
        self.num_of_sets = 0

    def add(self, val):
        if val not in self.parent:
            self.parent[val] = val ## parent[x] = x 表示 x 的 parent 是 x
            self.height[val] = 1
            self.num_of_sets += 1

    def find(self, val):
        '''
        get father of the val, return root of val
        假如我让你在上面的 parent 中找 0 的代表如何找？
        首先，树的根在 parent 中满足“parent[x] == x”。因此我们可以先找到 0 的父亲 parent[0] 也就是 1，
        接下来我们看 1 的父亲 parent[1] 发现是 3，因此它不是根，我们继续找 3 的父亲，发现是 3 本身。
        也就是说 3 就是我们要找的代表，我们返回 3 即可
        '''
        if val != self.parent[val]:  # 路径压缩 在查询的过程中，把沿途的每个节点的父节点都设为根节点
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

    def union_compress(self, x, y):
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

