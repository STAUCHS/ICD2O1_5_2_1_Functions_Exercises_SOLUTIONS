#-------------------------------------------------------------------------
# Name:       Pythagorean Theorem
# Purpose:		Function that calculates the hypotenuse of a right triangle
# Author:     Chen. C
# Created:    23/04/2024
#-------------------------------------------------------------------------

import math

""" Calculates the hypotenuse of a right triangle
Args:
  a (float): side a 
  b (float): side b

Returns:
  float: volume
"""

def hypotenuse(a: float, b: float) -> float:
  c = math.sqrt(a ** 2 + b ** 2)
  return c