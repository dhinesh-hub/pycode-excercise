#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
#DO NOT allocate another 2D matrix and do the rotation.
#Input: matrix = [[1,2,3],
#                 [4,5,6],
#                 [7,8,9]]
#Output: [[7,4,1],
#         [8,5,2],
#         [9,6,3]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#print(matrix[0][0])

n = len(matrix[0])
print (n // 2 + n % 2)
for i in range(0,n // 2):


tmp = matrix[0][0]
matrix[0][0] = matrix[2][0]
matrix[2][0] = matrix[2][2]
matrix[2][2] = matrix[0][2]
matrix[0][2] = tmp

tmp = matrix[0][1]
matrix[0][1] = matrix[1][0]
matrix[1][0] = matrix[2][1]
matrix[2][1] = matrix[1][2]
matrix[1][2] = tmp

#for i in range(0,len(matrix) - 1):
#    tmp = matrix[0][0]
#    matrix[0][0] = matrix[2][0]
#    matrix[2][0] = matrix[2][2]
#    matrix[2][2] = matrix[0][2]
#    matrix[0][2] = tmp

print(matrix)
