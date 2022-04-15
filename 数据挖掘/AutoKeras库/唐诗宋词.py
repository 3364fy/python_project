from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import autokeras as ak
data = fetch_20newsgroups(categories=['alt.atheism','soc.religion.christian', 'comp.graphics','sci.med']) #get with limited categories to save time
print(data)
# X_train, X_test, y_train, y_test = train_test_split(data['data'], data['target'], test_size=0.5) #split x and y w/ big test_size to save time
# X_train, X_test = np.array(X_train), np.array(X_test) #convert x-values (lists of strings) into arrays
# y_train, y_test = pd.get_dummies(y_train).values, pd.get_dummies(y_test).values #one-hot encode the y variables, which have four unique categories
# search = ak.TextClassifier(max_trials=3)
# search.fit(X_train, y_train)