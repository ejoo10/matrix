from matrix import *
from draw import *
from display import *
import math
import random

s = new_screen()
c = [ 255, 0, 0 ]

print("Testing add_edge, Adding (1, 2, 3), (4, 5, 6): m2 =")
m2 = [[], [], [], []]
add_edge(m2, [1, 2, 3], [4, 5, 6])
matrix_print(m2)
print("")

print("Testing identity: m1 =")
m1 = identity(4)
matrix_print(m1)
print("")

print("Testing matrix multiplication: m1 * m2 = ")
matrix_print(matrix_multiply(m1, m2))
print("")

print("m1 =")
m1 = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12], [1, 1, 1, 1]]
matrix_print(m1)
print("")

print("Testing matrix multiplication: m1 * m2 = ")
matrix_print(matrix_multiply(m1, m2))


edges = [[], [], [], []]
points = []
points.append([-1.54, 4.99, 0])
points.append([-1.76, -1.49, 0])
points.append([6.43, -1.49, 0])
points.append([0.44, -1.49, 0])
points.append([1.78, 2.29, 0])
points.append([2.44, 1.75, 0])
points.append([-1.65, 1.75, 0])
points.append([-1.69, 0.71, 0])
points.append([-2.69, 1.75, 0])
points.append([1.59, 1.75, 0])

add_edge(edges, points[0], points[1])
add_edge(edges, points[0], points[2])
add_edge(edges, points[1], points[2])
add_edge(edges, points[3], points[8])
add_edge(edges, points[3], points[4])
add_edge(edges, points[5], points[8])
add_edge(edges, points[1], points[9])
add_edge(edges, points[2], points[8])

scale = [[30, 0, 0, 250], [0, 30, 0, 250], [0, 0, 30, 250], [0, 0, 0, 1]]
edges = matrix_multiply(scale, edges)

draw_2D_edges(edges, s, c)
display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
