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

def is_correct(n: int, guess: int) -> bool:
  if n == guess:
    return True
  else:
    return False