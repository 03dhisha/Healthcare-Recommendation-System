import streamlit as st
import joblib
import pandas as pd
import health_data as hd

model = joblib.load('disease_model.pkl')
symptoms_list = joblib.load('symptom_columns.pkl')

st.title("Healthcare Recommendation System")
selected_symptoms = st.multiselect('Select your symptoms', symptoms_list)

if st.button('Predict'):
    input_data = {sym: 0 for sym in symptoms_list}
    for s in selected_symptoms:
        input_data[s] = 1
    df_input = pd.DataFrame([input_data])
    prediction = model.predict(df_input)[0]
    st.success(f"Predicted Disease: {prediction}")
    recos = hd.get_all_recos(prediction)
    st.write("Description:", recos['description'])
    st.write("Diet:", recos['diets'])
    st.write("Medications:", recos['medications'])
    st.write("Precautions:", recos['precautions'])
    st.write("Workout Tips:", recos['workouts'])