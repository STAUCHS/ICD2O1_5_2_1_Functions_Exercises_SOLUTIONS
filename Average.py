#-------------------------------------------------------------------------
# Name:       Average
# Purpose:		Function that calculates the average of four marks
# Author:		  Chen. C
# Created:    23/04/2024
#-------------------------------------------------------------------------

""" Calculates the average of four marks

Args:
  mark1 (float): first mark
  mark2 (float): second mark
  mark3 (float): third mark
  mark4 (float): fourth mark

Returns:
  float: average
"""

def average(mark1: float, mark2: float, mark3: float, mark4: float) -> float:
  sum = mark1 + mark2 + mark3 + mark4
  average = sum / 4
  return average