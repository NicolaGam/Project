import os       #streamlit run UI.py
import sys
sys.path.append(os.path.abspath('..'))
from src import config
import streamlit as st
import pickle

with open(f"{config.MODELS_PATH}RF_regression.pickle", "rb") as file:
    model = pickle.load(file)

with open(f"{config.MODELS_PATH}RF_regression_bonus.pickle", "rb") as file:
    model_bonus = pickle.load(file)

st.title("🏠 House Price Calculator")
st.divider()

options = ["Posizione📍", "Caratteristiche✨"]
selection = st.pills("Scegli che variabili utilizzare per il calcolo: ", options, selection_mode="single")
st.subheader("Inserisci i dati:")

if selection==options[0]:
     col1, col2 = st.columns(2)
     with col1:
         Latitude=st.number_input("🌍 Latitudine:")
     with col2:
         Longitude=st.number_input("🌍 Longitudine:")

     c1, c2, c3 = st.columns([2, 2, 1])

     with c2:
         if st.button("💰 Calcola Prezzo"):
             if Latitude>=25.01459 or Latitude<=24.93207 or Longitude<=121.47353 or Longitude>=121.56627 :
                with c1:
                     st.warning("inserisci delle coordinate valide")
             else:
                 X=[[Latitude,Longitude]]
                 prediction=model.predict(X)
                 with c1:
                     st.write("")
                     st.success(f"💰il prezzo stimato è: {prediction}per unità di area💰")

else:
    col1, col2 = st.columns(2)

    with col1:
         HouseAge=st.number_input("🏡 Età della casa (anni)")
    with col2:
         Distance= st.number_input("🚆 Distanza dalla MRT (metri)")
    Store=st.slider("🏪 Numero di minimarket nei dintorni", 0, 10, 1)
    
    
    c1, c2, c3 = st.columns([2, 2, 1])

    with c2:
        if st.button("💰 Calcola Prezzo"):
             X=[[HouseAge,Distance,Store]]
             prediction=model_bonus.predict(X)
             with c1:
                st.write("")
                st.success(f"💰il prezzo stimato è: {prediction} per unità di area💰")

st.divider()
st.text("Ti è stato utile questo strumento?")
stars = st.feedback("stars")


