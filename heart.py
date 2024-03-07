
import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open("C:/Users/soumya ranjan patro/trained_model.sav",'rb'))

def heart_disease(input_data):
    #changing the input data to numpy array

    input_data_as_numpy_array = np.asarray(input_data)
     # reshape the array as we are predicting for one instance input_data_reshaped input_data_as_numpy_array.reshape(1,-1)
    input_data_reshaped =input_data_as_numpy_array.reshape(1,-1) 

    prediction = loaded_model.predict(input_data_reshaped)

    print(prediction)

    if (prediction[0] == 0):
        return " No Heart Disease"
    else:
        return "Possibility of Heart Disease"
    
def main():
    
    st.title("HEART DISEASE PREDICTION WEB APP")
    col1 , col2 , col3 = st.columns(3)
    with col1:
        age = st.text_input("Enter Age")
    with col2:
        sex = st.text_input("Enter Sex(MAlE - 1 | FEMALE - 0)")
    with col3:
        cp  = st.text_input("Enter Chest Pain(1-4)")
    with col1:
        trestbps = st.text_input("Enter Blood Pressure")
    with col2:
        chol = st.text_input("Enter Cholestral(mg/dl)")
    with col3:
        fbs = st.text_input("Enter Fasting Blood Sugar(> 120 mg/dl)")
    with col1:
        restecg = st.text_input("Enter Resting ECG(0-2)")
    with col2:
        thalach = st.text_input("Enter Thalach") 
    with col3:
        exang = st.text_input("Enter Exang")
    with col1: 
        oldpeak = st.text_input("Enter Old Peak")
    with col2:
       slope = st.text_input("Enter Slope")
    with col3:
              ca = st.text_input("Enter Cardiac Arrest(0-3)")
    with col1:
        thal = st.text_input("Enter Thalassemia")
    
    #code for prediction
    diagnosis = " "
    
    if st.button("Do Prediction"):
        diagnosis=heart_disease([int(age),int(sex),int(cp),int(trestbps),int(chol),int(fbs),int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)])
    st.success(diagnosis)
    
if __name__=='__main__':
    main()


