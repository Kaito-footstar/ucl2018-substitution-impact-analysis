#Real Madrid's pass heatmap
#Bale go onto the pitch at the 60th minute

mask_realmadrid = (df['type_name'] == 'Pass') & (df['team_name'] == 'Real Madrid')
df_realmadrid_pass = df.loc[mask_realmadrid, ['x', 'y', 'end_x', 'end_y', 'minute']]

bale_minute = 60

before2 = df_realmadrid_pass[df_realmadrid_pass['minute'] <= bale_minute]
after2 = df_realmadrid_pass[df_realmadrid_pass['minute'] > bale_minute]

pitch = Pitch(line_color ='black')
fig, axs = pitch.grid(ncols = 2, grid_height = 0.9, title_height = 0.06, axis = False, endnote_height = 0.04, title_space = 0, endnote_space = 0)

bin_statistic3 = pitch.bin_statistic(before2.x, before2.y, bins =(16, 12), normalize = False)
pcm3 = pitch.heatmap(bin_statistic3, cmap ='Reds', edgecolor ='grey', ax = axs['pitch'][0])
axs['pitch'][0].set_title('Before Bale Substitution', fontsize = 16)

bin_statistic4 = pitch.bin_statistic(after2.x, after2.y, bins =(16, 12), normalize = False)
pcm4 = pitch.heatmap(bin_statistic4, cmap ='Reds', edgecolor ='grey', ax = axs['pitch'][1])
axs['pitch'][1].set_title('After Bale Substitution', fontsize = 16)
plt.show()
#2018clfinal_image_7.png
#---------------------------------------------------------------
#comment
"""
Liverpool's Salah was substituted due to an injury.
Salah is one of the most important player in Liverpool attack.
So, losing Salah was a huge damage for Liverpool.
You can see that by looking at the pass heat map.
In the pass heat map after the substitution, it seems that passes sere concentrated in the center and the right side where Mane was,
and there were probably fewer attacks coming from the left side.
But, after Real Madrid player Bale was substituted in and entered the pitch, there was no significant change in the pass heat map compared to before. 
This shows that Real Madrid’s attacks do not rely heavily on a single player. 
This does not mean that Bale was not an important asset. 
Bale scored two goals in a short amount of time, greatly contributing to the team’s attacking power and victory.
"""
