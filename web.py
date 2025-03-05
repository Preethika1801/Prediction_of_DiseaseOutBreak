import os
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# Set dark mode theme
st.set_page_config(page_title='Prediction System', layout='wide', page_icon='🧑‍⚕️')
st.markdown("""
    <style>
    body {
        background-color: #1E1E1E;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #333;
        color: white;
    }
    .stTextInput>div>div>input::placeholder {
        color: #bbb;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Load models
diabetes_model = pickle.load(open("C:/Users/jpree/OneDrive/Desktop/project/Prediction-of-Disease-Outbreaks/Training modules/diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("C:/Users/jpree/OneDrive/Desktop/project/Prediction-of-Disease-Outbreaks/Training modules/heart_model.sav", 'rb'))
parkinson_model = pickle.load(open("C:/Users/jpree/OneDrive/Desktop/project/Prediction-of-Disease-Outbreaks/Training modules/parkinson.sav", 'rb'))

# Top navigation bar
selected = option_menu(menu_title='',
                        options=['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Disease Prediction"],
                        icons=['activity', 'heart', 'person'],
                        menu_icon='cast',
                        default_index=0, orientation='horizontal')

def get_float_input(label, placeholder):
    value = st.text_input(label, placeholder=placeholder)
    if not value.strip():
        st.warning(f'⚠ Please enter a valid value for {label}')
        return None
    try:
        return float(value)
    except ValueError:
        st.error(f'❌ Invalid input for {label}. Please enter a number.')
        return None

if selected == 'Diabetes Prediction':
    st.title("🩸 Diabetes Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = get_float_input('Number of Pregnancies', 'e.g., 2')
        SkinThickness = get_float_input('Skin Thickness value', 'e.g., 23')
        DiabetesPedigreeFunction = get_float_input('Diabetes Pedigree Function', 'e.g., 0.572')
    with col2:
        Glucose = get_float_input('Glucose Level', 'e.g., 120')
        Insulin = get_float_input('Insulin Level', 'e.g., 80')
        Age = get_float_input('Age', 'e.g., 45')
    with col3:
        BloodPressure = get_float_input('Blood Pressure value', 'e.g., 72')
        BMI = get_float_input('BMI value', 'e.g., 28.4')

    if st.button("🔍 Get Diabetes Prediction") and all(v is not None for v in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        prediction = diabetes_model.predict([user_input])
        result = "🛑 The person is diabetic" if prediction[0] == 1 else "✅ The person is not diabetic"
        st.success(result)

elif selected == 'Heart Disease Prediction':
    st.title("❤️ Heart Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = get_float_input('Age', 'e.g., 45')
        trestbps = get_float_input('Resting Blood Pressure (mm Hg)', 'e.g., 120')
        restecg = get_float_input('ECG Results', 'e.g., 1')
        oldpeak = get_float_input('ST Depression', 'e.g., 2.3')
    with col2:
        sex = get_float_input('Sex (0: Female, 1: Male)', 'e.g., 1')
        chol = get_float_input('Cholesterol Level', 'e.g., 200')
        thalach = get_float_input('Max Heart Rate Achieved', 'e.g., 150')
        slope = get_float_input('ST Slope', 'e.g., 2')
    with col3:
        cp = get_float_input('Chest Pain Type (0-3)', 'e.g., 2')
        fbs = get_float_input('Fasting Blood Sugar (1: Yes, 0: No)', 'e.g., 0')
        exang = get_float_input('Exercise-Induced Angina (1: Yes, 0: No)', 'e.g., 0')
        ca = get_float_input('Major Vessels', 'e.g., 0')
        thal = get_float_input('Thalassemia', 'e.g., 3')

    if st.button("🔍 Get Heart Disease Prediction") and all(v is not None for v in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        prediction = heart_disease_model.predict([user_input])
        result = "🛑 The person has heart disease" if prediction[0] == 1 else "✅ The person does not have heart disease"
        st.success(result)

elif selected == "Parkinson's Disease Prediction":
    st.title("🧠 Parkinson's Disease Prediction using ML")
    cols = st.columns(5)
    inputs = [get_float_input(label, 'e.g., 0.5') for col, label in zip(cols * 5, ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'Spread1', 'Spread2', 'D2', 'PPE'])]
    
    if st.button("🔍 Get Parkinson's Prediction") and all(v is not None for v in inputs):
        prediction = parkinson_model.predict([inputs])
        result = "🛑 The person has Parkinson's disease" if prediction[0] == 1 else "✅ The person does not have Parkinson's disease"
        st.success(result)

