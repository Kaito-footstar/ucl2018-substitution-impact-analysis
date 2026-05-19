pitch = Pitch(line_color ='black')
fig, ax = pitch.grid(grid_height = 0.9, title_height = 0.06, axis =False, endnote_height =0.04, title_space =0, endnote_space =0)

mask_bale = (df.type_name == 'Shot') & (df.player_name =='Gareth Frank Bale')
df_bale_shots = df.loc[mask_bale, ['x', 'y', 'outcome_name', 'player_name']]

for i, row in df_bale_shots.iterrows():
    if row['outcome_name'] == 'Goal':
        pitch.scatter(row.x,row.y, alpha = 1, s = 500, color ='blue', ax = ax['pitch'])
        pitch.annotate(row['player_name'], (row.x + 1, row.y - 2),ax = ax['pitch'], fontsize = 12)
    else:
        pitch.scatter(row.x, row.y, alpha = 0.2, s = 500, color ='blue', ax = ax['pitch'])
#2018clfinal_image_4.png
#----------------------------------------------------
