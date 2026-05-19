!pip install mplsoccer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Pitch, Sbopen

parser = Sbopen()
df, related, freeze, tactics = parser.event(18245)

#sub player information
subs = df.loc[df['type_name'] == 'Substitution', ['minute', 'team_name', 'player_name']]
print(subs)
#2018clfinal_image_5.png
#----------------------------------------------------------

