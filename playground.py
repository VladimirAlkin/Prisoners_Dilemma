import strategy as s

#playground needed to stand 2 players against each other and start play
def playground(player1, player2):
  player1_result = player1.play()
  player2_result = player2.play()
  player1.update_score(player2_result)
  player2.update_score(player1_result)
  print('*'*25, '\n' f"{player1.strategy} VS {player2.strategy}!!!\n Player 1 choose to {player1_result}! \n Player 2 choose to {player2_result}! \n Score of {player1.strategy} player = {player1.points} \n Score of {player2.strategy} player = {player2.points}", '\n', '*'*25, '\n\n')

#results - name of strategy is a key and points are values
def strategy_results(players):
  # values indexes = 0 - all points, 1 - smallest one, 2 - biigest one
  # it's 1500 because it's the biggest possible score any player can get (15 per round * 100)
  final_results = {
  'Always Cooperate':[0, 1500, 0],
  'Always Defect': [0, 1500, 0],
  'Random choise':[0, 1500, 0],
  'Tit for Tat' : [0, 1500, 0],
  'Random Tit for Tat' : [0, 1500, 0]
  } 
    
  for player in players:
    scores = final_results[player.strategy]
    scores[0] += player.points
    if player.points < scores[1]:
      scores[1] = player.points  
    if player.points > scores [2]:
      scores[2] = player.points    
    final_results[player.strategy] = scores  
  return final_results


def create_players():
  players = []
  for i in range(0,20):
    players.append(s.strategy_coop())
  for i in range(0,20):
    players.append(s.strategy_defect())
  for i in range(0,20):
    players.append(s.strategy_random())
  for i in range(0,20):
    players.append(s.strategy_tit_for_tat())
  for i in range(0,20):
    players.append(s.strategy_tit_for_tat_rand())
  return(players)