# -*- coding: utf-8 -*-
import numpy as np

def main():
    s = input().strip()
    n, m, seed, num = map(int, s.split(','))
    np.random.seed(seed)
    A = np.random.randint(1, num+1, size=(n, m))
    print(A)
    print(np.dot(A, A.T))

if __name__ == "__main__":
    main()