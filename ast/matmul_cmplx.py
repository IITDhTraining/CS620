#CS620 Demo: This is an example input program to multiply two complex-valued matrices using Numpy library operation.
#Author: Nikhil Hegde
import numpy as np
def my_matmul(A: list[complex], B: list[complex]):
    C=np.matmul(A,B)
    print(C)

A: list[complex]=[[1,2,3],[4,5,6]]
B: list[complex]=[[1,4],[2,5],[3,6]]
my_matmul(A,B)
