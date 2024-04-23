#-------------------------------------------------------------------------
# Name:       Even or Odd
# Purpose:    Function that determines if a number is even, odd, or neither
# Author:     Chen. C
# Created:    23/04/2024
#-------------------------------------------------------------------------

""" Determines if a number is even, odd, or neither

Args:
  n (int): number

Returns:
  str: Neither, Even, or Odd
"""

def even_or_odd(n: int) -> str:
  if n == 0:
    return "Neither"
  elif n % 2 == 0:
    return "Even"
  else:
    return "Odd"