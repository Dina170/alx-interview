#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotate n x n 2D matrix 90 degrees clockwise in-place"""
    for i in range(len(matrix)):
        for j in range(1 + i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in matrix:
        i.reverse()
