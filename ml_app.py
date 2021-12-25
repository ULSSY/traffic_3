import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import seaborn as sb
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import OneHotEncoder
def run_ml_app() :
    df=pd.read_csv('data/도로교통.csv',encoding='CP949')
    X=df.loc[:,'사망자수']
    y=df['시도']
    X=df['사망자수']>10
    
    
    scaler_X=MinMaxScaler()
    X=scaler_X.fit_transform(X)
    y=pd.get_dummies(y)
    scaler_y=MinMaxScaler()
    y=scaler_y.fit_transform(y)
    X_train,y_train,X_test,y_test=train_test_split(X,y,test_size=0.25,random_state=22)
    regressor=RandomForestRegressor(random_state=50)
    regressor.fit(X_train,y_train)
    y_pred=regressor.predict(X_test)
    error=y_test-y_pred