import streamlit as st
import joblib
import pandas as pd

@st.cache_resource
def load_model():
    return joblib.load("Linear_Regression_model.joblib")

# Load trained model
model = load_model()


# Page title
st.title("Student Marks Prediction")

st.write(
    "Enter student information to predict marks."
)


col1, col2 = st.columns(2)

# Inputs
with col1:
    study_hours = st.number_input(
        "Study Hours",
        min_value=0,
        max_value=14,
        value=2
    )

    previous_score = st.number_input(
        "Previous Score",
        min_value=0,
        max_value=100,
        value=50
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=3,
        max_value=15,
        value=8
    )

with col2:
    extracurricular_activities = st.selectbox(
        "Extracurricular_Activities",
        options=("Yes","No"),
        index=None,
        placeholder="extracurricular activities participation ?"
    )


    internet_access = st.selectbox(
        "Internet Access",
        options=("Yes","No"),
        index=None,
        placeholder="has internet access ?"
    )

    student_motivation_level = st.selectbox(
        "Student Motivation Level",
        options=('Low', 'Medium', 'High'),
        index=None,
        placeholder="motivation level ?"
    )


# Prediction button
if st.button("Predict"):

    if (study_hours == None or 
    previous_score == None or 
    sleep_hours == None or 
    extracurricular_activities == None or 
    internet_access == None or
    student_motivation_level == None
    ):
        st.error("Each Field is Mandatory")


    else:

        features = pd.DataFrame([{
            'Study_Hours': study_hours,
            'Previous_Scores': previous_score,
            'Sleep_Hours': sleep_hours,
            'Extracurricular_Activities': extracurricular_activities, 
            'Internet_Access': internet_access,
            'Student_Motivation_Level': student_motivation_level
        }])

        score = model.predict(features)

        print(f"predicted score : {score[0]:.2f}")


        st.success(f"Student with above information is likely to score  **{score[0]:.2f}** Marks")


    # if prediction[0] == 1:
    #     st.success("Customer is likely to subscribe.")
    # else:
    #     st.error("Customer is unlikely to subscribe.")