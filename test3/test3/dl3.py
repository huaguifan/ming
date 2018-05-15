import math
import numpy as np
from sklearn.cluster import DBSCAN
iris = np.loadtxt('iris.txt', delimiter=',', usecols=(0, 1, 2, 3))
m, n = np.shape(iris)


def find_attractor(x_f, iris_f, h_f, e_f):
    p, q = np.shape(x_f)
    x_ti = np.zeros((p, q))
    k = np.zeros(p)
    k_x = np.zeros((p, q))
    x_t = np.zeros((p, q))
    x_t[0]=x_f
    for t in range(0, p):
        '''x_f = iris_f'''
        s1 = 0
        s2 = 0
        for i in range(0, p-1):
            x_ti[i] = x_f(t)-x_f(i)
            k_x[t] =  x_f(t) * math.exp(-(x_ti(i)) * (x_ti(i)) / (2 * h_f * h_f)) / math.sqrt(2 * math.pi)
            s1 = s1 + k_x[t]
            k[t] =  math.exp(-(x_ti(i)) * (x_ti(i)) / (2 * h_f * h_f)) / math.sqrt(2 * math.pi)
            s2 = s2 + k[t]
        x_f[t + 1] = s1 / s2
        if np.linalg.norm(x_f(t) - x_f(t-1)) <= e_f:
            return x_t(t)
    return x_t(t)


def den_clue(x_d, h_d, k_sin, e_d):
    p = np.shape(x_d)
    x_maximal = np.zeros((p))
    f_x = np.zeros(p)
    # k_sin = 1
    # e_d = 0.1
    # h_d = 1
    # d = q
    # min = 2
    k = np.zeros(p)
    x_ti = np.zeros((p))
    a_x = []
    r_x = []
    for i in range(1, p):
        x_maximal[i] = find_attractor(x_d[i], x_d, h_d, e_d)
        s = 0
        for j in range(1, p):
            x_ti[i] = x_maximal[i] - x_d[j]
            k[j] = math.exp(-(x_ti[j]) * (x_ti[j]) / (2 * h_d * h_d)) / math.sqrt(2 * math.pi)
            s = s + k[j]
        f_x[i] = s
        k = 0
        if f_x[i] >= k_sin:
            a_x[k] = x_maximal[i]
            r_x[k] = x_d[i]
            k = k + 1
    b = DBSCAN(eps=e_d, min_samples=min)
    c = b.fit_predict(np.mat(list(a_x)))
    return c


den_clue(iris[24], 5, 0.5, 0.01)
