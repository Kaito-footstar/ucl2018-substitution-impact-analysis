#Salah left the pitch at the 29th minute

#pass data before and after
mask_liverpool = (df['type_name'] == 'Pass') & (df['team_name'] == 'Liverpool')
df_liverpool_pass = df.loc[mask_liverpool, ['x', 'y', 'end_x', 'end_y', 'minute', 'player_name', 'pass_recipient_name']]

salah_minute = 29

before = df_liverpool_pass[df_liverpool_pass['minute'] <= salah_minute]
after = df_liverpool_pass[df_liverpool_pass['minute'] > salah_minute]

pitch = Pitch(line_color ='black')
fig, axs = pitch.grid(ncols=2, grid_height =0.9, title_height= 0.06, axis = False, endnote_height = 0.04, title_space = 0, endnote_space = 0)

bin_statistic1 = pitch.bin_statistic(before.x, before.y, bins = (16, 12), normalize = False)
pcm1 = pitch.heatmap(bin_statistic1, cmap = 'Reds', edgecolor ='grey', ax = axs['pitch'][0])
axs['pitch'][0].set_title('Before Salah Substitution', fontsize = 16)

bin_statistic2 = pitch.bin_statistic(after.x, after.y, bins =(16, 12), normalize = False)
pcm2 = pitch.heatmap(bin_statistic2, cmap ='Reds', edgecolor ='grey', ax = axs['pitch'][1])
axs['pitch'][1].set_title('After Salah Substitution', fontsize = 16)
plt.show()
#2018clfinal_image_6.png


#------------------------------------------------------
