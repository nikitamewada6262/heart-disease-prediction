import streamlit as st
import pandas as pd 
import joblib
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
</style>
""", unsafe_allow_html=True)
model = joblib.load("KNN_heart.pkl")
scaler =joblib.load("scaler.pkl")
excepted_columns= joblib.load("columns.pkl")
st.title("heart stroke prediction by Nikita❤️")
st.markdown("Your text here")
st.markdown("provide the following, details")
age=st.slider("age",18,100,40)
sex=st.selectbox("Sex",['M','F'])
chest_pain=st.selectbox("hest pain Type",["ATA","NAP","TA","ASY"])
resting_Bp=st.number_input("Restin Bloood Pressure(mm,hg)",80,200,120)
Cholesterol=st.number_input("Cholesterol(m/dl)",100,600,200)
FastingBS=st.selectbox("Fasting  Bloood sugar > 120 m/dl",[0,1])
RestingECG=st.selectbox("RestingECG",["Noraml","ST","LVh"])
max_hr= st.slider("MAx heart Rate",60,220,150)
ExerciseAngina=st.selectbox("Exercise-induced Angina",["Y","N"])
oldpeak = st.number_input("oldpeak(ST Depression)",0.0,6.0,1.0)
st_slope= st.selectbox("ST Slope",["UP","Flat","Down"])
if st.button("predict"):
    raw_input = {
        'Age':age,
        'Resting_Bp':resting_Bp,
        'Cholesterol':Cholesterol,
        'FastingBS':FastingBS,
        'Max_hr':max_hr,
        'Oldpeak':oldpeak,
        'Sex_'+ sex:1,
        'Chest_pain_type'+ chest_pain:1,
        'RestingECG'+RestingECG:1,
        'ExerciseAngina'+ ExerciseAngina:1,
        'ST_Slope_'+ st_slope:1


    }
    input_df =pd.DataFrame([raw_input])
    for col in excepted_columns:
        if col not in input_df.columns:
            input_df[col]=0


    input_df=input_df[excepted_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    if prediction == 1:
        st.error("⚠️high Risk of heart Disese")
    else:
        st.success("✅Low Risk of heart Disease")


    




