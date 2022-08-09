#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:
#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.

#Leetcode 36

board = [["2","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".",".","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","1","7"]]


freq_dict = {}
for i in range(0,9):
    for j in range(0,9):
       if board[i][j] == ".":
           continue
       elif freq_dict.get(board[i][j]):
           print("Not a valid Sudoku")
           exit(0)
       else:
           freq_dict[board[i][j]] = 1
    print(freq_dict)
    freq_dict.clear()

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
for j in range(0,9):
    for k in range (0,9):
        if board[k][j] == ".":
            continue
        elif freq_dict.get(board[k][j]):
            print("Not a valid Sudoku")
            exit(0)
        else:
            freq_dict[board[k][j]] = 1
    print(freq_dict)
    freq_dict.clear()
print("00000000000000000000000000000000000000000000000000000")
print(board[0][0:3])
print(board[1][0:3])
print(board[2][0:3])

for j in range(0,9,3):
   for i in range(0,9):
      if (i%3 == 0 and i > 0):
          print(".....................................")
          freq_dict.clear()
      else:
          for o in board[i][j:j+3]:
              if o == ".":
                  continue
              elif freq_dict.get(o):
                  print("Not a valid Sudoku")
                  exit(0)
              else:
                  freq_dict[o] = 1
      #print(freq_dict)
      print(board[i][j:j+3])


#print(board[0:3])
