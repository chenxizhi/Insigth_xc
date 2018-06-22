
from sklearn.externals import joblib
import pickle
import pandas as pd
import numpy as np

#load clf.v0
clf = joblib.load('GB_recall_optimized.pkl') 

def get_prediction(Company):
    X = pd.read_csv('features.csv')
    X = X.drop(X.columns[0],axis=1)
    cb_software_reddit = pd.read_csv('cb_reddit',sep="\t")
    cb_software_reddit = cb_software_reddit.drop(cb_software_reddit.columns[0],axis=1)
    X_query = X[cb_software_reddit.company_name == Company]
    print(X_query)
    if clf.predict(X_query).astype(int) == 0:
        blurb =  "NAY"
        color = "darkred"
    else:
        blurb = "YAY"
        color = "skyblue"
    return blurb, color



