import random

team_red = []
team_white = []
all_players = {}
all_fives = []
all_fours = []
all_threes = []
all_twos = []
all_fives_indices = []

y5 = random.randint(0,1)
y4 = random.randint(0,1)
y3 = random.randint(0,1)
y2 = random.randint(0,1)

def roster_players():
  number = int(input('How many players? '))
  for player in range(number):
    name = str(input('Name: '))
    rating = int(input('Rating: '))
    all_players[name] = rating
  

def sort_players():
  for player_name, value in all_players.items():
    if value == 5:
      all_fives.append(player_name)
    elif value == 4:
      all_fours.append(player_name)
    elif value == 3:
      all_threes.append(player_name)
    else:
      all_twos.append(player_name)
  print(all_fives)
  print(all_fours)
  print(all_threes)
  print(all_twos)

      
def show_teams():
  number = 1
  print("RED")
  for player in team_red:
    print(str(number) + '. ' + player)
    number = number + 1
  print(' ')
  print("WHITE")
  number = 1
  for player in team_white:
    print(str(number) + '. ' + player)
    number = number + 1


def add_fives():
  #if all_fives != []
    if len(all_fives) % 2 == 0:
      for i in range(int(len(all_fives)/2)):
        x = random.randint(0, len(all_fives)-1)
        team_red.append(all_fives[x])
        all_fives.remove(all_fives[x])
      for i in range(len(all_fives)):
        team_white.append(all_fives[i])
    else:
      for i in range(int(len(all_fives)/2) + y5):
        x = random.randint(0, len(all_fives)-1)
        team_red.append(all_fives[x])
        all_fives.remove(all_fives[x])
      for i in range(len(all_fives)):
        team_white.append(all_fives[i])





def add_fours():
  if len(all_fours) % 2 == 0:
    for i in range(int(len(all_fours)/2)):
      x = random.randint(0, len(all_fours)-1)
      team_red.append(all_fours[x])
      all_fours.remove(all_fours[x])
    for i in range(len(all_fours)):
      team_white.append(all_fours[i])

  else:
    for i in range(int(len(all_fours)/2) + y4):
      x = random.randint(0, len(all_fours)-1)
      team_red.append(all_fours[x])
      all_fours.remove(all_fours[x])
    for i in range(len(all_fours)):
      team_white.append(all_fours[i])


  
def add_threes():
  if len(all_threes) % 2 == 0:
    for i in range(int(len(all_threes)/2)):
      x = random.randint(0, len(all_threes)-1)
      team_red.append(all_threes[x])
      all_threes.remove(all_threes[x])
    for i in range(len(all_threes)):
      team_white.append(all_threes[i])
  else:
    for i in range(int(len(all_threes)/2) + y3):
      x = random.randint(0, len(all_threes)-1)
      team_red.append(all_threes[x])
      all_threes.remove(all_threes[x])
    for i in range(len(all_threes)):
      team_white.append(all_threes[i])



  
def add_twos():
  if len(all_twos) % 2 == 0:
    for i in range(int(len(all_twos)/2)):
      x = random.randint(0, len(all_twos)-1)
      team_red.append(all_twos[x])
      all_twos.remove(all_twos[x])
    for i in range(len(all_twos)):
      team_white.append(all_twos[i])
  else:
    for i in range(int(len(all_twos)/2) + y2):
      x = random.randint(0, len(all_twos)-1)
      team_red.append(all_twos[x])
      all_twos.remove(all_twos[x])
    for i in range(len(all_twos)):
      team_white.append(all_twos[i])
  



  
def create_teams():
  sort_players()
  add_fives()
  add_fours()
  add_threes()
  add_twos()
  show_teams()
  


def new_teams():
  global red_rating
  global white_rating
  global all_fives
  global all_fours
  global all_threes
  global all_twos
  global team_red
  global team_white
  all_fives = []
  all_fours = []
  all_threes = []
  all_twos = []
  team_red = []
  team_white = []
  red_rating = 0
  white_rating = 0
  create_teams()
  

def clear_roster():
  global all_players
  all_players = {}

roster_players()
create_teams()
