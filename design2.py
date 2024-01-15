# supply program prolog (3 P's)
# Prolog
# Kylie Orozco
# Purpose: Two-player dice game called Twenty One
# Pre-cond: User inputs names of both players, each player takes turns choosing pass or roll
# Post-cond: Program will output amount rolled, amount of passes remaining, and who won at the end 

import random


def play_turn(player_name,player_total_roll,player_pass_Count):
  Answer=pass_or_roll(player_name)
  if(Answer=="P" and player_pass_Count>0):
    player_pass_Count-=1
    print("Player {} passed the roll".format(player_name) )
  else:
    rolled=roll_dice()
    print("Player {} rolled a {}".format(player_name,rolled) )
    player_total_roll+=rolled
  return 3-player_pass_Count,player_total_roll
 
    

def check(total):
  flag=False
  if(total>=21 ):
    flag=True
  return flag

  
def pass_or_roll(player_name):
  answer=input("Player {} (P)ass or (R)oll? ".format(player_name))
  while(answer.upper()!="P" and answer.upper()!="R"):
    answer=input("Invalid response, P or R please ")

  return answer.upper()


def roll_dice():
  random.seed(25)
  return (random.randint(1, 6))
  

def main():

  # title / instructions
  print("Don't get to 21!")
  print();
  print("Each player tries not to get to 21")
  print("Each player has 3 passes, which allow them to not roll on a round.")
  
  # get players' names
  p1 = input("Who is player 1? ")
  p2 = input("Who is player 2? ")
  print();
  
  # do setup = initialization, etc.
  winner = ''
  round = 1
  player_count = 1
  p1_total = 0
  p2_total = 0
  p1_pass = 3
  p2_pass = 3  
  
  # while neither player has lost
  while(True):
    print("Round {}:".format(round))
    if(player_count==1):
      p1_total, p1_pass = p1_total, p1_pass
      p1_pass_count, p1_total = play_turn(p1, p1_total, p1_pass)
      if(check(p1_total)):
        winner = p2
        break
      player_count+=1
    else:
      p2_total, p2_pass = p2_total, p2_pass
      p2_pass, p2_total = play_turn(p2, p2_total, p2_pass)
      if(check(p2_total)):
        winner = p1
        break
      player_count-=1
      print("{} total roll {} passes {}  |  {} total roll {} passes {}".format(p1, p1_total, p1_pass, p2, p2_total, p2_pass))
      
      print();
      # display the round number
      round+=1
      
    #announce who won
  print();
  print("{} won!".format(winner))
    
main()