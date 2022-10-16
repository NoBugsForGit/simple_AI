# 生成机器学习样本
# _*_ coding:UTF-8 _*_
import random as r


def willing(size):
    sample = []
    for i in range(0, size):
        quality = ((r.randint(0, 100)) / 100) + 0.3
        needing = ((r.randint(0, 100)) / 100) + 0.5
        evaluation = ((r.randint(0, 100)) / 100) + 0.7
        value = r.randint(1, 10000)
        expectation = int(quality * needing * evaluation * value)
        price = r.randint(1, 31000)
        if expectation >= price:
            will = True
        else:
            will = False
        sample.append([quality, needing, evaluation, value, will])
    return sample
