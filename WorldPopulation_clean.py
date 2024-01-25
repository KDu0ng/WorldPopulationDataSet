import pandas as pd
import numpy as np

# read in all our data
nfl_data = pd.read_csv("world_population.csv")

# set seed for reproducibility
np.random.seed(0) 

nfl_data.head()