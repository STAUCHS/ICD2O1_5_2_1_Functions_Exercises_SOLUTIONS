#-------------------------------------------------------------------------
# Name:		    Attendance
# Purpose:	  Function that lets the user know how long they will need to wait during roll call
# Author:		  Chen. C
# Created:		23/04/2024
#-------------------------------------------------------------------------

""" Let's user know their wait time during roll call

Args:
  last_name (str): last name

Returns:
  str: sentence about the wait time
"""

def attendance(last_name: str) -> str:
  if last_name <= "carswell":
    return "You don't have to wait long."
  elif last_name <= "jones":
    return "That's not bad"
  elif last_name <= "smith":
    return "Looks like a bit of a wait."
  elif last_name <= "young":
    return "It's gonna be a while."
  elif last_name > "young":
    return "Not going anywhere for a while."