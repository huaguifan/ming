
import os
import types
import math
import sys
import numpy as np

C = []


class node:
    purity = 0
    label = ""
    left_node = None
    right_node = None
    data = []
    children = []
    split_point = 0
    split_index = 0

    def __init__(self, label="", data=[], purity=0):
        self.label = label
        self.data = data
        self.purity = purity



# #纯净度
def purity(n_i, n):
    temp = 0
    temp_index = 0
    for i in range (len(n_i)):
        if n_i[i]/n > temp:
            temp = n_i[i]/n
            temp_index = i
    return temp, temp_index


# #可能分支
def P_ciD_Y(n_vi, n_v):
    sum = 0
    for j in range(len(n_v)):
        # #所有点的和
        sum += n_v[j]
        # #Y中点除以所有点
    ans = n_vi/sum
    return ans


# #N中可能性
def P_ciD_N(n_vi, n_v, n_ii, n_i):
    sum = 0
    for j in range(len(n_v)):
        # #所有的点减去Y点
        sum += n_i[j] - n_v[j]
    if sum == 0:
        return 0
    return (n_ii-n_vi)/sum


# #D中可能性
def P_ciD(c_index, D):
    c_sum = 0
    for i in range(len(D)):
        if D[i][-1] == C[c_index]:  # #由标签知道是哪一类
            c_sum += 1

    return c_sum/len(D)


# #D中ci的熵函数
def Entropy(D):
    Entropy_sum = 0
    for j in range(len(C)):
        if P_ciD((j, D)):
            continue
        Entropy_sum -= P_ciD(j, D)*math.log(P_ciD(i, D), 2)

    return Entropy_sum


# #信息增益函数
def Gain(G_D, G_DY, G_DN):
    n = len(G_D)
    n_Y = len(G_DY)
    n_N = len(G_DN)
    gain = Entropy(G_D) - n_Y/n*Entropy(F_DY)-n_N/n*Entropy(G_DY)
    return gain


# #数字属性
def Evaluate_NU_umeric_Attribute(D, x_i):
    n_v = [0]*len(C)
    D = sorted(D, key=lambda x: x[x_i])
    M = set()
    n_i = [0]*len(C)    # #初始化类个数
    for j in range(len(D)-1):  # #D中除最后一个的每个点
        for i in range(len(C)):  # #判断属于哪一类
            if D[j][-1] == C[i]:
                n_i[i] += 1  # #找到该类 点数加1
            if D[j+1][x_i] != D[j][x_i]:
                v = (D[j+1][x_i] + D[j][x_i])/2  # #中间点
                M.add(v)  # #加入集合
            for i in range(len(C)):
                n_v[i] = n_i[i]

        if D[len(D)-1][-1] == C[i]:
            n_i[i] += 1
    v_star = 0
    score_star = 0
    p_ciD_Y=[0]*len(c)
    p_ciD_N=[0]*len(c)

    for v in M:  # #对集合中的每个midpoint进行判断
        for i in range(len(C)):
            p_ciD_Y = P_ciD_Y(n_v[i], n_v)  # #属于ci类且为Y的可能性
            p_ciD_N = P_ciD_N(n_v[i], nv, n_i[i], n_i)  # #属于ci类且为N的可能性
        DY = []  # #记录Y中的点
        DN = []  # #记录N中的点
        for j in range(len(D)):
            if D[j][xi] <= v:  # #小于V即为Y
                DY.append(D[j])  # #插入列表中
            else:
                DN.append(D[j])

        score_minv = Gain(D, DY, DN)  # #算出得分
        if score_minv > score_star:
            v_star = v
            score_star = score_minv
        return v_star, score_star


# #决策树主函数
def DecisionTree(D, leaf_size, pi, root):
    n = len(D)
    n_i = [0]*len(C)
    for i in range(len(C)):
        for j in range(n):
            if D[j][-1] == c[i]:
                n_i[i] += 1

    purity_D, purity_index = purity(n_i, n)  # #计算纯净度
    print("purity", purity_D)
    if n <= leaf_size or purity_D > pi:  # #如果小于叶节点数或纯净度大于要求就转化为叶节点
        C_star = C[purity_index]
        root.C_label = C_star
        root.data = D
        root.purity = purity_D
        return

    splitpoint_star = 0
    score_star = 0
    split_index = 0
    for i in range(len(D[0]-1)):  # #对每个数字属性进行评估打分
        v, score = Evaluate_NU_umeric_Attribute(D, i)
        # #让score为最大得分
        if score > score_star:
            score_star = score
            splitpoint_star = v
            split_index = i
    root.splitpoint_star = splitpoint_star
    root.splitpoint_index = split_index
    # #输出internal node
    print("internal node", v)
    Dy = []
    Dn = []
    for i in range(len(D)):  # #将Y和N中的点存入列表中
        if D[i][split_index] <= splitpoint_star:
            Dy.append(D[i])
        else:
            Dn.append(D[i])
    Ynode = node
    Nnode = node
    root.left = Ynode  # #左子节点
    root.right = Nnode  # #右子节点
    print("Dy", len(Dy), Dy)
    print("Dn", len(Dn), Dn)
    DecisionTree(Dy, leaf_size, pi, root.left)  # #嵌套调用
    DecisionTree(Dn, leaf_size, pi, root.right)


if __name__ == "__main__":

    # def readFile(a):  # #读取txt中的数据
    #     a = "iris.txt"
    #     f = open(a, "r", encoding="utf-8")
    #     F = []
    #     for line in f:
    #         s = line.strip().split(",")
    #         label = s[-1]
    #         if label.strip() not in C:
    #             C.append(label.strip())
    #         F.append(s)
    #     return F
    # a = "iris.txt"
    # D = readFile(a)  # #读取数据

    D = np.loadtxt('iris.txt', delimiter=',', usecols=(0, 1, 2, 3))


    # for i in range(len(D)):
    #     for j in range(len(D[0])-1):
    #         D[i][j] = (float(D[i][j]))  # #D中数字由字符串转为float
    root = node
    DecisionTree(D, 5, 0.95, root)

