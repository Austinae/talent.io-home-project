# ### Part 1: Volleyball simulation *(Backend)*

# The objective is to write a program that simulates a game of Volleyball between Team 1 and Team 2.

# The program takes 2 inputs:
# - p1 = The probability that Team 1 wins the point when Team 1 is serving
# - p2 = The probability that Team 2 wins the point when Team 2 is serving

# The rules:
# 1. To win the match, a team must win 3 sets.
# 2. To win a set, a team must win at least 25 points with a 2-points margin minimum, e.g. 25-17, 24-26, 28-26.
# 3. Exception to rule #2: If both teams are tied at 2 sets, the fifth and last set ends in 15 points, again with a 2-points margin minimum.
# 4. Team 1 starts serving in set 1, Team 2 starts serving in set 2, Team 1 starts serving in set 3, and so on.
# 5. The team that won the previous point serves for the next point, unless the set is just starting.

# The output of the program is the list of scores, from the beginning to the end of the game.

# Example, if team 1 wins all points:

# ```rb
# VolleyballSimulator.run(1.0, 0.0) == [
#   "0-0", # Game starts
#   "1-0", # Team 1 wins 1st point
#   "2-0",
#   # ...
#   "25-0",
#   "25-0 1-0",
#   "25-0 2-0",
#   # ...
#   "25-0 25-0",
#   "25-0 25-0 1-0",
#   "25-0 25-0 2-0",
#   # ...
#   "25-0 25-0 25-0" # Game ends
# ]
# ```

import random

#
class VolleyballSimulator(object):
  """ A class which mimics a volleyball game and prints out score at each point interval """

  def __init__(self, p1, p2):
    """ Initialize the VolleyballSimulator class from manual input or stdin """

    if not isinstance(p1, float):
      raise TypeError("p1 must be float")
    if not isinstance(p1, float):
      raise TypeError("p1 must be float")

    self.p1 = p1                 #The probability that Team 1 wins the point when Team 1 is serving
    self.p2 = p2                 #The probability that Team 2 wins the point when Team 2 is serving
    self.servePriority = 0       #Tracks who needs to serve next, 0 for Team 1, 1 for Team 2
    self.p1Set = 0               #Number of sets won by Team 1
    self.p2Set = 0               #Number of sets won by Team 2
    self.p1Points = 0            #Number of points won in set by Team 1 
    self.p2Points = 0            #Number of points won in set by Team 2
    self.score = []              #Agglomeration of set scores

  
  def playPoint(self):
    """ Virtually plays a point according to probability given in self.p1 and self.p2 """

    p = self.p1 if self.servePriority == 0 else self.p2
    if random.random() < p:
      if self.servePriority == 0:
        self.p1Points += 1
      else:
        self.p2Points += 1
    else:
      if self.servePriority == 0:
        self.p2Points += 1
        self.servePriority = 1
      else:
        self.p1Points += 1
        self.servePriority = 0

  def displayScore(self, includePoints):
    """ Prints out score at any given point """

    for sett in self.score:
      print(str(sett[0])+'-'+str(sett[1]), end=' ')
    if includePoints is True:
      print(str(self.p1Points)+'-'+str(self.p2Points))

  def play(self):
    """ Main function of this class, runs through the game rules detailed above """

    while self.p1Set < 3 and self.p2Set < 3:
      print("Game ", len(self.score)+1, " is about to start")
      maxPoints = 15 if len(self.score) == 4 else 25
      self.servePriority = 0 if len(self.score)%2 == 0 else 1
      while self.p1Points < maxPoints and self.p2Points < maxPoints:
        self.playPoint()
        if self.p1Points == self.p2Points and maxPoints - self.p1Points == 1:
          maxPoints += 1
        self.displayScore(True)
      if self.p1Points == maxPoints:
        self.p1Set += 1
      else:
        self.p2Set += 1
      self.score.append((self.p1Points, self.p2Points))
      self.p1Points = 0
      self.p2Points = 0
    if self.p1Set == 3:
      print("Game is over, team 1 wins, score is :")
      self.displayScore(False)
    else:
      print("Game is over, team 2 wins, score is :")
      self.displayScore(False)


def main():
  #STDIN
  # p1 = float(input("Please a float value between 0.0 and 1.0 inclusive, the probability that Team 1 wins the point when Team 1 is serving: "))
  # p2 = float(input("Please a float value between 0.0 and 1.0 inclusive, the probability that Team 1 wins the point when Team 2 is serving: "))
  
  #Manual input
  p1 = float(1.0)
  p2 = float(0.0)

  vbg = VolleyballSimulator(p1, p2)
  vbg.play()
 
if __name__ == '__main__':
  main()