# -*- coding: utf-8 -*-
"""2018CLfinal.ipynb

I created this program 2025/11/20.
But I created this repository on this account 2026/04/29.
Because I changed account to this account from previous one.

I made this program on Google Colaboratory.

I wrote comment on practice_python_7. 
"""


#Champions League Final RealMadrid vs Liverpool

#Analysis of Liverpool and Real Madrid in the 2018 UCL Final, focusing on attacking patterns before and after key player substitutions.

#showed all passes by each player
!pip install mplsoccer
import numpy as np
import matplotlib.pyplot as plt
from mplsoccer import Pitch, Sbopen

parser = Sbopen()
df, related, freeze, tactics = parser.event(18245)

#--------------------------------------------------
#collected Real Madrid's pass data
mask_real_madrid = (df['type_name'] == 'Pass') & (df['team_name'] == 'Real Madrid') & (df['sub_type_name'] != 'Throw-in')
df_RMA_passes = df.loc[mask_real_madrid, ['x', 'y', 'end_x', 'end_y', 'player_name']]
RMA_names = df_RMA_passes['player_name'].unique()

#drowed pitch shape
pitch = Pitch(line_color ='black', pad_top =20)
fig, axs = pitch.grid(ncols = 4, nrows = 4, grid_height = 0.85, title_height = 0.06, axis = False, endnote_height = 0.04, title_space = 0.04, endnote_space = 0.01)

for name, ax in zip(RMA_names, axs['pitch'].flat[:len(RMA_names)]):
    ax.text(60, -10, name, ha ='center', va ='center', fontsize =9)
    player_df = df_RMA_passes.loc[df_RMA_passes['player_name'] == name]
    pitch.scatter(player_df.x, player_df.y, alpha = 0.2, color ='blue', ax = ax)
    pitch.arrows(player_df.x, player_df.y, player_df.end_x, player_df.end_y, color ='blue', ax = ax, width = 1)

for ax in axs['pitch'][-1, 16 - len(RMA_names):]:
    ax.remove()
#2018clfinal_image_1.png

#---------------------------------------------------
