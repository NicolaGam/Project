import os       #streamlit run UI.py
import sys
sys.path.append(os.path.abspath('..'))
from src import config
import streamlit as st
import pickle

with open(f"{config.MODELS_PATH}knn_regression.pickle", "rb") as file:
    model = pickle.load(file)

with open(f"{config.MODELS_PATH}knn_regression_bonus.pickle", "rb") as file:
    model_bonus = pickle.load(file)

st.title("House Price Calculator")
st.divider()

options = ["Latitude, Longitude", "House Age, Distance to MRT, Number of Convenience Store"]
selection = st.pills("Decidi che variabili utilizzare:", options, selection_mode="single")

if selection==options[0]:
     Latitude=st.number_input("inserisci la latitudine:")
     Longitude=st.number_input("inserisci la longitudine:")
     if st.button("Calcola"):
         if Latitude>=25.01459 or Latitude<=24.93207 or Longitude<=121.47353 or Longitude>=121.56627 :
             st.warning("inserisci delle coordinate valide")
         else:
             X=[[Latitude,Longitude]]
             prediction=model.predict(X)
             st.success(f"il prezzo stimato è: {prediction}")

else:
     HouseAge=st.number_input("inserisci l'età dell'abitazione")
     Distance= st.number_input("inserisci la distanza dalla stazione MRT più vicina")
     Store=st.number_input("inserisci il numero di minimarket nei dintorni")
     if st.button("Calcola"):
         X=[[HouseAge,Distance,Store]]
         prediction=model_bonus.predict(X)
         st.success(f"il prezzo stimato è: {prediction}")

