#-------------------------------------------------------------------------
# Name:       Sum If Different
# Purpose:		Function that sums unique values
# Author:		  Chen. C
# Created:    23/04/2024
#-------------------------------------------------------------------------

""" Sum unique values from three numbers

Args:
  x (int): first number
  y (int): second number
  z (int): third number

Returns:
  int: sum
"""

def sum_if_diff(x: int, y: int, z: int) -> int:
  # Sum the unique values
  # All numbers are different
  if (x != y) and (y != z) and (x != z):
    sum = x + y + z

  # a and b are the same - sum = a + c 
  elif (x == y) and (x != z) and (y != z):
    sum = x + z

  # a and c are the same - sum = a + b
  elif (x == z) and (x != y) and (y != z):
    sum = x + y

  # b and c are the same - sum = a + b
  elif (x != y) and (x != z) and (y == z):
    sum = x + y

  # All numbers are the same
  else:
    sum = x

  return sum