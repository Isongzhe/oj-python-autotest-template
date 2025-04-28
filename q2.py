# -*- coding: utf-8 -*-
import numpy as np

def main():
    seed = int(input().strip())
    np.random.seed(seed)
    A = np.random.randint(11, 50, size=(3, 6))
    print(A)
    print(f"The mean for the matrix is: {A.mean():.2f}")
    for i, row in enumerate(A):
        print(f"The mean for row {i} is: {row.mean():.2f}")
    for j, col in enumerate(A.mean(axis=0)):
        print(f"The mean for column {j} is: {col:.2f}")

if __name__ == "__main__":
    main()