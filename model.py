import pandas as pd
import numpy as np
import pickle
k= pd.read_csv("processed_data.csv")
df = pd.DataFrame(k)
X =df[['White Rating', 'Black Rating', 'accdiff', 'misdiff', 'blundiff']].values
y =df['Winner'].values
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X,y)
pickle.dump(lr,open("model.pkl","wb"))



 