
#collected Liverpool's pass data
mask_liverpool = (df['type_name'] == 'Pass') & (df['team_name'] == 'Liverpool') & (df['sub_type_name'] != 'Throw-in')
df_LIV_passes = df.loc[mask_liverpool, ['x', 'y', 'end_x', 'end_y', 'player_name']]
LIV_names = df_LIV_passes['player_name'].unique()

pitch = Pitch(line_color ='black', pad_top =20)
fig, axs = pitch.grid(ncols = 4, nrows = 4, grid_height = 0.85, title_height = 0.06, axis = False, endnote_height = 0.04, title_space = 0.04, endnote_space = 0.01)

for name, ax in zip(LIV_names, axs['pitch'].flat[:len(LIV_names)]):
    ax.text(60, -10, name, ha ='center', va ='center', fontsize =9)
    player_df = df_LIV_passes.loc[df_LIV_passes['player_name'] == name]
    pitch.scatter(player_df.x, player_df.y, alpha = 0.2, color ='blue', ax = ax)
    pitch.arrows(player_df.x, player_df.y, player_df.end_x, player_df.end_y, color ='blue', ax = ax, width = 1)

for ax in axs['pitch'][-1, 16 - len(LIV_names):]:
    ax.remove()
#2018clfinal_image_2.png

#-------------------------------------------------

