#-------------------------------------------------------------------------
# Name:       Fahrenheit to Celsius
# Purpose:    Function that converts fahrenheit to celsius
# Author:     Chen. C
# Created:    23/04/2024
#-------------------------------------------------------------------------

""" Converts Fahrenheit to Celsius

Args:
  F (float): fahrenheit

Returns:
  float: celcius
"""

def FtoC(F: float) -> float:
  celsius = (5/9) * (F - 32)
  return celsius