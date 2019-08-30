import pandas as pd 
import numpy as np 

# Load the data
oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')
gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',', delimiter='\t',
                             encoding='latin1', na_values="n/a")

print(oecd_bli)
np.array(oecd_bli)
print(np.array(oecd_bli))
