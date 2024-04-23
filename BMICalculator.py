#-------------------------------------------------------------------------
# Name:		    BMI Calculator
# Purpose:	  Function that determines health range based on BMI
# Author:     Chen. C
# Created:		23/04/2024
#-------------------------------------------------------------------------

""" Determines healthy range based on BMI

Args:
  h (float): height
  w (float): weight

Returns:
  str: health range
"""

def BMI(h: float, w: float) -> str:
  bmi = w / (h**2)

  if BMI < 19:
    return "You are below the healthy range."
  elif BMI <= 25: 
    return "You are within the healthy range."
  else:
    return "You are above the healthy range."