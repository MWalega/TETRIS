from dataclasses import dataclass
import random
from copy import deepcopy

# BOARD

# - list of lists with integers
# - size always 10x20
# - 0: empty field
# - 1: shape
# - 2: border of board
# - 5 upper rows serve as place to input shape
# - game over if board contains 1 on row <= 5

board = [[2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,2,2,2,2,2,2,2,2,2],]

# SHAPES

# - size of list of list with shape is always 5x5
# - 0: empty field, 1: shape
# - allshapes are stored on list called 'shapes'
# - every shape is a list containing list of lists containing integers. Every
#   list of lists depict unique rotation of certain shape
# - list contain every possible shape's rotation
# - when rotating shape change rotation in order of list positions
# - when last rotation changes -> jump to the start of the list and shape is
#   in start rotation 

S = [[[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,1,1,0],
      [0,1,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,1,0],
      [0,0,0,1,0],
      [0,0,0,0,0]]]

Z = [[[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,0,0],
      [0,0,1,1,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,1,1,0,0],
      [0,1,0,0,0],
      [0,0,0,0,0]]]
 
I = [[[0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [1,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]]
 
O = [[[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,0,0],
      [0,1,1,0,0],
      [0,0,0,0,0]]]
     
J = [[[0,0,0,0,0],
      [0,1,0,0,0],
      [0,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,1,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,0,0,1,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,1,1,0,0],
      [0,0,0,0,0]]]
 
L = [[[0,0,0,0,0],
      [0,0,0,1,0],
      [0,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,1,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,1,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,1,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]]
 
T = [[[0,0,0,0,0],
      [0,0,1,0,0],
      [0,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,1,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,1,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]]

shapes = [S, Z, I, O, J, L, T]

# CLASSES

@dataclass
class pos:
  row: int
  col: int

@dataclass
class LiveShape:
  shape_ind: int # in range(len(shapes))
  shape_rot: int # in range(len(shapes[shape_ind]))
  current_pos: pos

# FUNCTIONS

def pick_new_random_shape() -> LiveShape:
  shape_ind = random.randint(0, len(shapes) - 1)
  starting_pos = pos(0, 3) 
  ls = LiveShape(shape_ind, 0, starting_pos)
  return ls

def print_board(board, ls: LiveShape):
  board_to_print = deepcopy(board)
  
  # adding current shape to board_to_print
  for srow in range(5):
    for scol in range(5):
      if shapes[ls.shape_ind][ls.shape_rot][srow][scol] == 1:
        assert(board_to_print[ls.current_pos.row + srow][ls.current_pos.col + scol] == 0)
        # - current_pos is the position of shapes[shape_ind][current_rot][0][0] on board 
        #   (ie upper left corner)
        # - current_pos+delta is the position of shapes[shape_ind][current_rot][delta.row][delta.col]
        #   on board (ie upper left corner)
        board_to_print[ls.current_pos.row + srow][ls.current_pos.col + scol] = 1

  # printing board_to_print
  for row in board_to_print:
    print(row)

def rotate_shape(ls: LiveShape) -> LiveShape:
  old_ls = deepcopy(ls)
  ls.shape_rot = (ls.shape_rot + 1)%(len(shapes[ls.shape_ind]))
  return old_ls

def move_shape(ls: LiveShape, input_move = 's') -> LiveShape:
  old_ls = deepcopy(ls)
  delta_pos = {
   's' : pos(1, 0), 
   'a' : pos(0, -1),
   'd' : pos(0, 1),
   '' : pos(0, 0),
  }

  assert input_move in ['a', 's', 'd', '']
  change_pos(ls, delta_pos[input_move])

  return old_ls

def change_pos(ls: LiveShape, delta: pos):
  ls.current_pos.row += delta.row
  ls.current_pos.col += delta.col

def check_if_collide(ls: LiveShape, board) -> bool:
  for srow in range(5):
    for scol in range(5):
      if (shapes[ls.shape_ind][ls.shape_rot][srow][scol] == 1 and 
          board[ls.current_pos.row + srow][ls.current_pos.col + scol] == 1 or
          board[ls.current_pos.row + srow][ls.current_pos.col + scol] == 2):
        return True
  return False

def add_shape_to_board(ls: LiveShape, board):
  for srow in range(5):
    for scol in range(5):
      if shapes[ls.shape_ind][ls.shape_rot][srow][scol] == 1:
        board[ls.current_pos.row + srow][ls.current_pos.col + scol] = 1

def remove_full_rows(board):
  len_row_no_border = len(board[0][1:-1])
  
  for i in range(len(board[5:])):
    count = 0
    for j in range(1, len(board[i][:-1])):
      if board[i][j] == 1:
        count += 1
    if count == len_row_no_border:
      remove_row_and_adapt_board(board, i)
      remove_full_rows(board)

def remove_row_and_adapt_board(board, i: int):
  # cleaning full i-row
  for j in range(1, len(board[0][:-1])):
    board[i][j] = 0

  # pulling down all 1's above i-row by 1
  for x in range(len(board[i]), 5, -1):
    for y in range(1, len(board[0][:-1])):
      if board[x][y] == 1:
        board[x][y], board[x+1][y] = 0, 1

def check_if_game_over(board) -> bool:
  for i in range(5):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        return False
  return True

def tetris(board, shapes):
  is_running = True
  is_moving = False
  ls = pick_new_random_shape()

  while is_running:
    print_board(board, ls)
    input_move = input('w-rotate, a-left, d-right, None-nothing')
    assert input_move in ['w','a','d','']
    if input_move == 'w':
      old_ls = rotate_shape(ls)
    else:
      old_ls = move_shape(ls, input_move)
    collision = check_if_collide(ls, board)
    if collision:
      ls = old_ls
    old_ls = move_shape(ls)
    collision = check_if_collide(ls, board)
    if collision:
      ls = old_ls
      add_shape_to_board(ls, board)
      remove_full_rows(board)
      ls = pick_new_random_shape()
      is_running = check_if_game_over(board)
  return 'Game over'

tetris(board, shapes)
