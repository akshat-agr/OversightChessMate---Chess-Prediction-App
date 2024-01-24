import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

k= pd.read_csv("chess.csv")
df = pd.DataFrame(k)
df = df.drop(df.columns[0:2], axis=1)
df.info()
df.describe()

df = df.drop(columns=['Opening ECO'])
df = df.drop(columns=['Opening Ply'])
df = df.drop(columns=["White Centi-pawn Loss"])
df = df.drop(columns=["Black Centi-pawn Loss"])
df.shape

df['accdiff'] = df["White's Number of Inaccuracies"] - df["Black's Number of Inaccuracies"]
df['misdiff'] = df["White's Number of Mistakes"] - df["Black's Number of Mistakes"]
df['blundiff'] = df["White's Number of Blunders"] - df["Black's Number of Blunders"]
df = df.drop(df.columns[2:8], axis=1)
df = df[['White Rating', 'Black Rating', 'accdiff', 'misdiff', 'blundiff','Winner']]


X =df[['White Rating', 'Black Rating', 'accdiff', 'misdiff', 'blundiff']].values
y =df['Winner'].values
