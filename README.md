# 🏥 Healthcare Recommendation System  

An **AI-powered healthcare assistant** built with **Streamlit** and **Random Forest** for **disease prediction and personalized health recommendations**.  
The system takes **symptom inputs** from users, predicts the most probable disease, and provides **relevant recommendations** like description, diet, medications, precautions, and workout tips.  

## 🔑 Features  
- **Symptom-based Prediction**  
  Select multiple symptoms and get the predicted disease using a trained Random Forest model.  
- **Personalized Recommendations**  
  Provides disease-specific:  
  - 📖 Description  
  - 🥗 Diet plans  
  - 💊 Medications  
  - ⚠️ Precautions  
  - 🏋️ Workout tips  
- **Machine Learning Pipeline**  
  - Data preprocessing (`prepare_data.py`)  
  - Model training (`train_model.py` / `model_training.py`)  
  - Symptom encoding and feature generation  
  - Trained model (`disease_model.pkl`) and feature list (`symptom_columns.pkl`)  
- **Interactive Dashboard**  
  Built with **Streamlit** for an easy-to-use interface.

## Install dependencies:
pip install -r requirements.txt
## Prepare training data (optional, if you want to rebuild):
python prepare_data.py
## Train the model (optional):
python train_model.py
## Run the Streamlit app:
streamlit run app.py
