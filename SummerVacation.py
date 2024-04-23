#-------------------------------------------------------------------------
# Name:       Summer Vacation
# Purpose:		Function that checks if user can go on summer vacation and where
# Author:		  Chen. C
# Created:    23/04/2024
#-------------------------------------------------------------------------

""" Determines summer vacation status

Args:
  avg (float): average mark
  income (float): income before summer

Returns:
  int: sum
"""

def summer_vacay(avg: float, income: float) -> str:
  if avg >= 80 and income >= 500:
    return "Congratulations! You can go to Europe in the summer." 
  elif avg >= 80:
    return "Well done! You can go to California in the summer." 
  else:
    return "Sorry, you cannot go on vacation this summer." 