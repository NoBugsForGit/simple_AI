# 进行机器学习
# _*_ coding:UTF-8 _*_
# 返回0说明样本不可信

def learn(sample, size):
    AQ = [0, 0]
    AN = [0, 0]
    AE = [0, 0]
    AV = [0, 0]
    A0 = 0
    A1 = 0
    for i in range(0, size):
        if sample[i][-1]:
            AQ[0] += sample[i][0]
            AN[0] += sample[i][1]
            AE[0] += sample[i][2]
            AV[0] += sample[i][3]
            A0 += 1
        else:
            AQ[1] += sample[i][0]
            AN[1] += sample[i][1]
            AE[1] += sample[i][2]
            AV[1] += sample[i][3]
            A1 += 1
    if A0 == 0 or A1 == 0:
        return 0
    else:
        AQ[0] /= A0
        AN[0] /= A0
        AE[0] /= A0
        AV[0] /= A0
        AQ[1] /= A1
        AN[1] /= A1
        AE[1] /= A1
        AV[1] /= A1
        standard = [[AQ[0], AN[0], AE[0], AV[0], True], [AQ[1], AN[1], AE[1], AV[1], False]]
        return standard
