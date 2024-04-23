#-------------------------------------------------------------------------
# Name:       Guessing Game
# Purpose:    Function that determines a guess is correct
# Author:     Chen. C
# Created:    23/04/2024
#-------------------------------------------------------------------------

""" Determines if number and guess is equal

Args:
  n (int): random number
  guess (int): guess

Returns:
  bool: if guess is correct, return True
"""

def letter_grade(mark: float) -> str:
  if mark >= 80 and mark <= 100:
    return "A"
  elif mark >= 70 and mark < 80:
    return "B"
  elif mark >= 60 and mark < 70:
    return "C"
  elif mark >= 50 and mark < 60:
    return "D"
  elif mark >= 0 and mark < 50:
    return "F"
  else:
    return "Invalid input. Mark must be between 0 and 100."