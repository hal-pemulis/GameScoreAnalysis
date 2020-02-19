# GameScoreAnalysis

import csv

game_info = {}

comments = []


with open('metacritic_game_info.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter = ',')

    header_info = next(csvreader)


    for row in csvreader:
        game_info.update({row[1] : {'MetaScore' : row[6], 'Average user score' : row[7], 'Year' : row[2], 'Platform': row[5]}})
        

    f.close()

with open('metacritic_game_user_comments.csv', 'r') as g:
    reader = csv.reader(g, delimiter = ',')

    header_comments = next(reader)

    for row in reader:
        comments.append(row[1])

    g.close()

for game in game_info:
    comment_count = 0
    for comment in comments:
        if game == comment:
            comment_count += 1
    game_info[game].update('Number of MetaCritic comments') = comment_count

print(game_info)
  
        
        

        
