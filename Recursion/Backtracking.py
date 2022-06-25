## backtracking
# 常被用于搜索排列组合问题的所有可能性
# 不同于普通的暴力搜索，回溯法会在每一步判断状态是否合法 而不是等到状态全部生成后再进行确定
# 当某一步状态非法时 它将退到上一步中正确的位置 然后继续搜索


## 什么时候需要startIndex
#  从左向右取数，取过的数，不在重复取

## 取过的位置不再取
## 使用startIndex
## 216.Combination Sum I https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(startIndex, path):
            if sum(path) == n and len(path) == k:
                res.append(path[:])
                # return
            # 剪枝
            if sum(path) >n or len(path) > k:
                return
            for i in range(startIndex, 10):
                if startIndex>n:
                    break
                path.append(i)
                backtrack(i+1, path) #这里是i+1
                path.pop()
        backtrack(1, [])
        return res


# 同一树层去重 如何判断同一树层上元素（相同的元素）是否使用过了呢？
# used
# 如果candidates[i] == candidates[i - 1] 并且 used[i - 1] == false
# 就说明：前一个树枝，使用了candidates[i - 1]，也就是说同一树层使用过candidates[i - 1]


# 40 Combination Sum II  https://leetcode.com/problems/combination-sum-ii/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        - 原数组有重复 所以同一树层要去重
        - 回溯时需要从下一位取 所以需要startindex 但同一树枝可以取val相同的树
        - 需要剪枝
        '''
        candidates.sort()
        res = []
        used = [0] * len(candidates)

        def backtrack(startIndex, path):
            if sum(path) == target:
                res.append(path[:])
                # return
            # 同#39题剪枝
            if sum(path) > target:
                return
            for i in range(startIndex, len(candidates)):
                if i > 0 and used[i - 1] == 0 and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                used[i] = 1
                backtrack(i + 1, path)
                used[i] = 0
                path.pop()
        backtrack(0, [])
        return res


# 90. Subsets II https://leetcode.com/problems/subsets-ii/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        - 原数组有重复 所以同一树层要去重
        - 回溯时需要从下一位取 所以需要startindex 但同一树枝可以取val相同的树
        - 无需剪枝
        '''
        res = []
        nums.sort()
        used = [0] * len(nums)

        def backtrack(startIndex, path):
            res.append(path[:])
            # 这里为什么不能return
            # 有return 直接 return [[]]
            for i in range(startIndex, len(nums)):
                if i > 0 and used[i - 1] == 0 and nums[i] == nums[i - 1]:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                used[i] = 0

        backtrack(0, [])
        return res


# 同一树枝去重






## 剪值
# 39. Combination Sum https://leetcode.com/problems/combination-sum/
# 树枝剪枝，已经知道下一层的sum会大于target，就没有必要进入下一层递归了

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        - 原数组没有有重复 所以同一树层不需要去重
        - 回溯时可以取当前位置 元素可无限重复选取
        - 需要剪枝
        '''
        res = []

        def backtrack(startIndex, path):
            if sum(path) == target:
                res.append(path[:])
                # return
            # 已经知道下一层的sum会大于target，就没有必要进入下一层递归了
            if sum(path) > target:
                return

            for i in range(startIndex, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path)
                path.pop()

        backtrack(0, [])
        return res

