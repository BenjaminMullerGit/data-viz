import helpers
import datetime
import pandas as pd
from sklearn import preprocessing
from sklearn.externals import joblib
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline, TransformerMixin
import sklearn.cross_validation as cv
from sklearn.linear_model import Lasso
from sklearn.linear_model import BayesianRidge
from sklearn.externals import joblib
from sklearn.svm import SVR

import bb_transformer   

# Load DF 
db_helper = helpers.Helpers()
db_helper.db_connect()
df = db_helper.load_into_panads()

df2 = df[["latitude", "longitude"]]
df2.to_json("output.json", orient="records")
