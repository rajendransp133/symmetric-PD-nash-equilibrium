import numpy as np
import math
import pandas as pd


class prisoner:

  def __init__(self,reward,sucker,temptation,penalty,action_x,action_y):
    RR=(reward,reward)
    ST=(sucker,temptation)
    TS=(temptation,sucker)
    PP=(penalty,penalty)
    act=[action_x,action_y]
    n=[RR,ST,TS,PP]
    m = np.array(n, dtype=[("x", object), ("y", object)])
    self.actions=act
    self.size=int(math.sqrt(len(n)))
    self.scores = m.reshape(self.size,self.size)
    self.row_labels = self.generate_labels(self.size)
    self.col_labels = self.generate_labels(self.size)
    self.corr={0:'C',1:'D'}

  def generate_labels(self, labels_num):
    return list(range(labels_num))


  def matrixPrint(self):
    game = pd.DataFrame(np.nan, self.actions, self.actions, dtype=object)
    for i in range(self.size):
      for j in range(self.size):
        game.iat[i, j] = self.scores[i][j]
    print(game)
  

  def equilibrium(self):

    best_payouts = {}
    max_payout=0

    for c in range(self.size):
      if(self.scores[0][c][0]<self.scores[1][c][0]):
        max_payout=self.scores[1][c][0]
      else:
        max_payout=self.scores[0][c][0]
      for r in range(self.size):
        if self.scores[r][c][0] == max_payout:
          best_payouts[(r, c)] = (self.row_labels[r], self.col_labels[c])

    max_payout=0
    best_payout_labels = []

    for r in range(self.size):
      if(self.scores[r][0][1]<self.scores[r][1][1]):
        max_payout=self.scores[r][1][1]
      else:
        max_payout=self.scores[r][0][1]
      for c in range(self.size):
        if self.scores[r][c][1] == max_payout:
          if (r, c) in best_payouts:
            best_payout_labels.append(best_payouts[(r, c)])

    return best_payout_labels


  def nashEq(self):
    equilibriums = self.equilibrium()
    for s in equilibriums:
        print("Player 1 plays", self.corr[s[0]], "and Player 2 plays", self.corr[s[1]])
    if len(equilibriums) == 0:
        print("No pure strategies")

  def dominant(self):
    max_ele=0
    for c in range(self.size):
      for r in range(self.size):
        if(self.scores[r][c][0]>max_ele):
          row_pos=r
          max_ele=self.scores[r][c][0]
      save_row=row_pos
    if(row_pos==save_row):
      print(self.corr[row_pos]+" is dominant strategy")
    


p=prisoner(3,0,5,1,'C','D')
p.matrixPrint()
p.nashEq()
p.dominant()


#  https://github.com/david138/Nash-Equilibrium/tree/master/src
#  https://github.com/cristal-smac/ipd