#showed both team's shots map
pitch = Pitch(line_color ='black')
fig, ax = pitch.grid(grid_height = 0.9, title_height = 0.06, axis =False, endnote_height = 0.04, title_space = 0, endnote_space = 0)

#Real Madrid's shots
mask_realmadrid = (df.type_name == 'Shot') & (df.team_name =='Real Madrid')
df_RMA_shots = df.loc[mask_realmadrid, ['x', 'y', 'outcome_name', 'player_name']]

for i, row in df_RMA_shots.iterrows():
    if row['outcome_name'] == 'Goal':
        pitch.scatter(row.x, row.y, alpha = 1, s = 500, color ='blue', ax = ax['pitch'])
        pitch.annotate(row['player_name'], (row.x + 1, row.y - 2), ax = ax['pitch'], fontsize = 12)
    else:
        pitch.scatter(row.x, row.y, alpha = 0.2, s = 500, color ='blue', ax = ax['pitch'])

#Liverpool's shots
mask_shots_liverpool = (df.type_name == 'Shot') & (df.team_name == 'Liverpool')
df.LIV_shots = df.loc[mask_shots_liverpool, ['x', 'y', 'outcome_name', 'player_name']]

for i, row in df.LIV_shots.iterrows():
    if row['outcome_name'] == 'Goal':
        pitch.scatter(120 - row.x, 80 - row.y, alpha = 1, s = 500, color ='red', ax = ax['pitch'])
        pitch.annotate(row['player_name'], (120 - row.x + 1,80 - row.y - 2), ax= ax['pitch'], fontsize = 12)
    else:
        pitch.scatter(120 - row.x, 80 - row.y, alpha = 0.2, s = 500, color = 'red', ax = ax['pitch'])

fig.suptitle('Real Madrid (blue) and Liverpool (red) shots', fontsize = 30)
plt.show()
#2018clfinal_image_3.png

#-------------------------------------------------
