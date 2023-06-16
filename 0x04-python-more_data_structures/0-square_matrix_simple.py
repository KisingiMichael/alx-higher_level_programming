#!/usrr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda z: list(map(lambda x: x * x, z)),matrix))
