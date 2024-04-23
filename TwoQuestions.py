#-------------------------------------------------------------------------
# Name:       Two Questions
# Purpose:		Function that determines answer to two questions
# Author:		  Chen. C
# Created:    23/04/2024
#-------------------------------------------------------------------------

""" Determines answer to two questions

Args:
  q1 (str): Answer to question 1 (animal, vegetable, or mineral)
  q2 (str): Answer to question 2 (bigger than a bread box, y or n)

Returns:
  str: Guess 
"""

def two_qs(q1: str, q2: str) -> str:
  # Decide on answer
  if q1 == "animal":
    if q2 == "y":
      return "My guess is that you are thinking of a moose."
    else:
      return "My guess is that you are thinking of a squirrel." 

  elif q1 == "vegetable":
    if q2 == "y":
      return "My guess is that you are thinking of a cabbage." 
    else:
      return "My guess is that you are thinking of a tomato." 

  else:
    if q2 == "y":
      return "My guess is that you are thinking of a car." 
    else:
      return "My guess is that you are thinking of a paper clip." 