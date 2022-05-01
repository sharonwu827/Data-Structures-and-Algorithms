# backtracking
# 常被用于搜索排列组合问题的所有可能性
# 不同于普通的暴力搜索，回溯法会在每一步判断状态是否合法 而不是等到状态全部生成后再进行确定
# 当某一步状态非法时 它将退到上一步中正确的位置 然后继续搜索


def backtracking(idx, cur, path):
    '''
    :param idx: 当前位置
    :param cur: 当前路径的某个信息
    :param path: 路径
    :return: 结果集
    '''
    # 找到解
    if cur == target:
        ans.append(path.copy())]
        return
    # 搜索完毕
    if idx == n:
        return
    for num in nums:
        if num == error or num in visited:
            continue
        visited.add(num)
        path.append(num)
        backtracking(idx+1, cur+num, path)

        path.pop()
        visited.remove(num)
