import playground as p
import random

print("Algorithm to find best strategy for Prisoner's dilemma.\n More points a strategy gets - worse it is. \n 5 strategys we have: \n 1) Allways cooperate - allways cooperate with a second player \n 2)Allways defect - allways betray a second player \n 3)Random choise - randomly choosing to defect or cooperate \n 4) Tit for tat - choosing to betray or cooperate on base what other played chose in a previous round \n 5) Tit for tat with random - same thing as tit for tat only have 1% probality of choosing cooperate when defect have to be \n You will get results printed and also - a .txt file with results table.\n\n PRESS ENTER TO START")
input()

players_circle_1 = p.create_players()
players_circle_2 = random.sample(players_circle_1,50) #choose 50 randon players
players_circle_1 = [x for x in players_circle_1 if x not in players_circle_2] #delete 50 players from circle 1 to not repeat them
random.shuffle(players_circle_1)



for r in range (0,70):
  random.shuffle(players_circle_1)
  random.shuffle(players_circle_2)
  for i in range (0,50):
    p.playground(players_circle_1[i],players_circle_2[i])
    

played_players = players_circle_1 + players_circle_2
results_dict = p.strategy_results(played_players)


for k,v in results_dict.items():
  print(k, end=' --- ')
  print('score: ',v[0],'average: ',v[0]/20 , ' minimum: ',v[1], ' maximum: ',v[2])

with open ('result_table.txt', 'w') as f:
 for k,v in results_dict.items():
   line = f"{k} --- score: {v[0]} average: {v[0]/20} minimum: {v[1]} maximum {v[2]} \n"   
   f.write(line)

   
