import random

COOPERATE = "Cooperate"
DEFECT = "Defect"


class strategy_coop():
  def __init__(self):
    self.strategy = 'Always Cooperate'
    self.points = 0
    self.my_last_play = COOPERATE
    self.last_opponent_reaction = COOPERATE

  def play(self):    
      return COOPERATE
  
  def update_score(self, opponent_reaction):
    self.last_opponent_reaction = opponent_reaction
    points_to_add = cal_score(self.my_last_play, opponent_reaction)
    self.points += points_to_add 
  
  def __str__(self):
    return f"{self.strategy}:  {self.points}"
  
  def __repr__(self):
    return f"{self.strategy}:  {self.points}"

class strategy_defect():
  def __init__(self):
    self.strategy = 'Always Defect'
    self.points = 0
    self.my_last_play = DEFECT
    self.last_opponent_reaction = COOPERATE

  def play(self):
      return DEFECT
  
  def update_score(self, opponent_reaction):
    self.last_opponent_reaction = opponent_reaction
    points_to_add = cal_score(self.my_last_play, opponent_reaction)
    self.points += points_to_add

  def __str__(self):
    return f"{self.strategy}:  {self.points}"
  
  def __repr__(self):
    return f"{self.strategy}:  {self.points}"

class strategy_random():
  def __init__(self):
    self.strategy = 'Random choise'
    self.points = 0
    self.my_last_play = COOPERATE
    self.last_opponent_reaction = COOPERATE

  def play(self):
      self.my_last_play = random.choice([COOPERATE, DEFECT])
      return self.my_last_play
  
  def update_score(self, opponent_reaction):
    self.last_opponent_reaction = opponent_reaction
    points_to_add = cal_score(self.my_last_play, opponent_reaction)
    self.points += points_to_add

  def __str__(self):
    return f"{self.strategy}:  {self.points}"
  
  def __repr__(self):
    return f"{self.strategy}:  {self.points}"

class strategy_tit_for_tat():
  def __init__(self):    
    self.strategy = 'Tit for Tat'
    self.points = 0
    self.my_last_play = COOPERATE
    self.last_opponent_reaction = COOPERATE

  def play(self):
    if self.last_opponent_reaction == DEFECT:
      self.my_last_play = DEFECT
      return DEFECT
    else:
      self.my_last_play = COOPERATE
      return COOPERATE 
  
  def update_score(self, opponent_reaction):
    self.last_opponent_reaction = opponent_reaction
    points_to_add = cal_score(self.my_last_play, opponent_reaction)
    self.points += points_to_add
    if points_to_add == 1:
      self.last_opponent_reaction = COOPERATE    
    elif points_to_add == 5:
      self.last_opponent_reaction = DEFECT  
    elif points_to_add == 15:
      self.last_opponent_reaction = DEFECT     
    else:
      self.last_opponent_reaction = COOPERATE 
      
  def __str__(self):
    return f"{self.strategy}:  {self.points}"
  
  def __repr__(self):
    return f"{self.strategy}:  {self.points}"

class strategy_tit_for_tat_rand():
  def __init__(self): 
    self.strategy = 'Random Tit for Tat'   
    self.points = 0
    self.my_last_play = COOPERATE
    self.last_opponent_reaction = COOPERATE

  def play(self):
    if self.last_opponent_reaction == DEFECT and random.random() == 0.01:
      self.my_last_play = COOPERATE
      return COOPERATE
    elif self.last_opponent_reaction == DEFECT:
      self.my_last_play = DEFECT
      return DEFECT
    else:
      self.my_last_play = COOPERATE
      return COOPERATE 
  
  def update_score(self, opponent_reaction):
    self.last_opponent_reaction = opponent_reaction
    points_to_add = cal_score(self.my_last_play, opponent_reaction)
    self.points += points_to_add
    if points_to_add == 1:
      self.last_opponent_reaction = COOPERATE    
    elif points_to_add == 5:
      self.last_opponent_reaction = DEFECT  
    elif points_to_add == 15:
      self.last_opponent_reaction = DEFECT     
    else:
      self.last_opponent_reaction = COOPERATE

  def __str__(self):
    return f"{self.strategy}:  {self.points}"
  
  def __repr__(self):
    return f"{self.strategy}:  {self.points}"


def cal_score(player_1_reaction, player_2_reaction):      
  scores = {} #dict with scores as valuse and strings of reactions as keys
  with open("config.txt", 'r') as conf:
    for line in (conf.readlines()):
      line = line.split(',')
      scores[line[0]+line[1]] = int(line[2])  

  return scores[player_1_reaction + player_2_reaction]