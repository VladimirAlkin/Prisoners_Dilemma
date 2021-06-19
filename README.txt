Algorithm for choosing a strategy for a Prisoner's dilemma 

5 strategys  - 5 classes. 
Allways cooperate*, allways defect**, random choise, tit for tat and tit for tat with 1% probality of choosing cooperate instead of defect
The more points a strategy gets, the worse it is 
The conditions for obtaining points are described in the configuration file
Configuration file note - first choise in the config is for player it self and second - for the second player.

Algorithm:
We create 100 players - 20 of each strategy
We divide them into 50 random pairs and make them play against each other
After all players played - the round is over. We have 100 rounds.
At the end we get printed results  table and file with it
Result table contains - score of all 20 players of a strategy, avarege score for player, player with minimum score for this strategy and player with maximum score

More details in comments for the code

*Cooperate - means cooperate with the second player and not with the "system"
**Defect - means betray second player

@ALkin Vladimir
