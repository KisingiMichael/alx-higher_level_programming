#!/usr/bin/python3
"""Create pascal triangle function"""


def pascal_triangle(n):
    """create a list to represent the pascal triangle"""
    triangles = []
    if n == 0:
        return (triangles)

    triangles.append([1])

    for i in range(1, n):
        tri_before = triangles[-1]
        tri_after = [1]
        for i in range(len(tri_before) - 1):
            tri_after.append(tri_before[i] + tri_before[i + 1])
        tri_after += [1]
        triangles.append(tri_after)
    return triangles
