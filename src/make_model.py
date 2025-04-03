from src import config
import sqlite3
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import os
import sys
from sklearn.neighbors import KNeighborsRegressor
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path

import logging
# Set up logging



def load_data():
    """Loads data from the SQLite database."""
    query = f"SELECT * FROM {config.RAW_TABLE}"
    conn= sqlite3.connect(config.DATABASE_PATH)
    db = pd.read_sql_query(query, conn)
    conn.close()
    return db


def train_model():
    """Trains a Random Forest model with GridSearchCV and saves evaluation metrics to CSV."""
    df = load_data()


    X = df[['Latitude','Longitude']]
    y = df['HousePrice']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )


    model=KNeighborsRegressor(n_neighbors=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

     # Saving random forest in pickle format
    logging.info('saving Knn regression...')
    with open(os.path.join(config.MODELS_PATH, "knn_regression.pickle"), "wb") as file:
        pickle.dump(model,file)



def train_model_bonus():
    """Trains a Random Forest model with GridSearchCV and saves evaluation metrics to CSV."""
    df = load_data()


    X = df[['HouseAge','DistancetoMRT','NumOfConvStore']]
    y = df['HousePrice']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )


    model=KNeighborsRegressor(n_neighbors=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

     # Saving random forest in pickle format
    logging.info('saving Knn regression...')
    with open(os.path.join(config.MODELS_PATH, "knn_regression_bonus.pickle"), "wb") as file:
        pickle.dump(model,file)



  
