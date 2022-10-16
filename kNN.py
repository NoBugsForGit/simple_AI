# 按kNN算法进行计算
# _*_ coding:UTF-8 _*_
# 返回0说明学习结果不可信

def dis(a, b):
    if len(a) != len(b):
        return -1
    else:
        c = len(a)
        result = 0
        for i in range(0, c):
            result += ((a[i] - b[i]) ** 2)
        result **= 0.5
        return result


def cal(sta, datas):
    size = len(sta)
    if size < 2:
        return 0
    error = 0
    for i in datas:
        re = [1000000, True]
        for j in sta:
            a = dis(i, j)
            if a < re[0]:
                re[0] = a
                re[1] = j[-1]
        if re[1] != i[-1]:
            error += 1
    return error
