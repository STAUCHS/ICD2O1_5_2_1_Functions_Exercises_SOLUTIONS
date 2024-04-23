#-------------------------------------------------------------------------
# Name:       Volume of Cone
# Purpose:		Function that calculates the volume of a cone
# Author:		  Chen. C
# Created:    23/04/2024
#-------------------------------------------------------------------------
import math

""" Calculates the volume of a cone

Args:
  r (float): radius
  h (float): height

Returns:
  float: volume
"""

def cone_volume(r: float, h: float) -> float:
  volume = (math.pi * (r ** 2) * h) / 3
  return volume