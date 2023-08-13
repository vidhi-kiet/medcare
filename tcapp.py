# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 16:24:09 2023

@author: vidhi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model

diabetes_model=pickle.load(open('C:/Users/vidhi/OneDrive/Desktop/multidesise dataset - Copy/diabetes.sav','rb'))

heart_disease_model=pickle.load(open('C:/Users/vidhi/OneDrive/Desktop/multidesise dataset - Copy/heart_disease_model.sav','rb'))

parkinsons_model=pickle.load(open('C:/Users/vidhi/OneDrive/Desktop/multidesise dataset - Copy/parkinsons_model.sav','rb'))

Breast_cancer_model=pickle.load(open('C:/Users/vidhi/OneDrive/Desktop/multidesise dataset - Copy/breast_cancer_model.sav','rb'))

#sidebar for navigation

with st.sidebar:
    
    selected =option_menu('TotalCare Disease Predictor',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction','Breast Cancer Prediction'],
                          icons=['activity','heart-pulse-fill','person','virus']
                          ,default_index=0)
    
    
    
    
    
#diabetes prediction page
if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    
    
    #getting input data from user
    #column for input fields
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number Of Pregnancies')
        
    with col2:
        Glucose=st.text_input('Glucose Level')  
        
    with col3:
        BloodPressure=st.text_input('BloodPressure value')
  
    with col1:
        SkinThickness=st.text_input('SkinThickness')

    with col2:
        Insulins=st.text_input('Insulin Level')
        
    with col3:
        BMI=st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age=st.text_input('Age of the Person')

        

   # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulins, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The Person is Diabetic'
        else:
          diab_diagnosis = 'The Person is Not Diabetic'
        
    st.success(diab_diagnosis)



    
    
if(selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        age = float(age)
        sex = float(sex)
        cp = float(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = float(fbs)
        restecg = float(restecg)
        thalach = float(thalach)
        exang = float(exang)
        oldpeak = float(oldpeak)
        slope = float(slope)
        ca = float(ca)
        thal = float(thal)
         
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
    
if(selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        
            # Convert input values to numeric
            fo = float(fo)
            fhi = float(fhi)
            flo = float(flo)
            Jitter_percent = float(Jitter_percent)
            Jitter_Abs = float(Jitter_Abs)
            RAP = float(RAP)
            PPQ = float(PPQ)
            DDP = float(DDP)
            Shimmer = float(Shimmer)
            Shimmer_dB = float(Shimmer_dB)
            APQ3 = float(APQ3)
            APQ5 = float(APQ5)
            APQ = float(APQ)
            DDA = float(DDA)
            NHR = float(NHR)
            HNR = float(HNR)
            RPDE = float(RPDE)
            DFA = float(DFA)
            spread1 = float(spread1)
            spread2 = float(spread2)
            D2 = float(D2)
            PPE = float(PPE)

            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
            if (parkinsons_prediction[0] == 1):
              parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
              parkinsons_diagnosis = "The person does not have Parkinson's disease"
              
          
            st.success(parkinsons_diagnosis)

    
if selected == 'Breast Cancer Prediction':
    
    #page title
    st.title('Breast Cancer Prediction using ML')
    col1, col2, col3 = st.columns(3)  
    
    with col1:
        radius_mean = st.text_input('Mean Radius')
        texture_mean = st.text_input('Mean Texture')
        perimeter_mean = st.text_input('Mean Perimeter')
        area_mean = st.text_input('Mean Area')
        smoothness_mean = st.text_input('Mean Smoothness')
        compactness_mean = st.text_input('Mean Compactness')
        concavity_mean = st.text_input('Mean Concavity')
        concave_points_mean = st.text_input('Mean Concave Points')
        symmetry_mean = st.text_input('Mean Symmetry')
        fractal_dimension_mean = st.text_input('Mean Fractal Dimension')
        
    with col2:
        radius_se = st.text_input('Radius Error')
        texture_se = st.text_input('Texture Error')
        perimeter_se = st.text_input('Perimeter Error')
        area_se = st.text_input('Area Error')
        smoothness_se = st.text_input('Smoothness Error')
        compactness_se = st.text_input('Compactness Error')
        concavity_se = st.text_input('Concavity Error')
        concave_points_se = st.text_input('Concave Points Error')
        symmetry_se = st.text_input('Symmetry Error')
        fractal_dimension_se = st.text_input('Fractal Dimension Error')
        
    with col3:
        radius_worst = st.text_input('Worst Radius')
        texture_worst = st.text_input('Worst Texture')
        perimeter_worst = st.text_input('Worst Perimeter')
        area_worst = st.text_input('Worst Area')
        smoothness_worst = st.text_input('Worst Smoothness')
        compactness_worst = st.text_input('Worst Compactness')
        concavity_worst = st.text_input('Worst Concavity')
        concave_points_worst = st.text_input('Worst Concave Points')
        symmetry_worst = st.text_input('Worst Symmetry')
        fractal_dimension_worst = st.text_input('Worst Fractal Dimension')
    
    # code for Prediction
    Breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        try:
            # Convert and validate input values
            radius_mean = float(radius_mean) if radius_mean else None
            texture_mean = float(texture_mean) if texture_mean else None
            perimeter_mean = float(perimeter_mean) if perimeter_mean else None
            area_mean = float(area_mean) if area_mean else None
            smoothness_mean = float(smoothness_mean) if smoothness_mean else None
            compactness_mean = float(compactness_mean) if compactness_mean else None
            concavity_mean = float(concavity_mean) if concavity_mean else None
            concave_points_mean = float(concave_points_mean) if concave_points_mean else None
            symmetry_mean = float(symmetry_mean) if symmetry_mean else None
            fractal_dimension_mean = float(fractal_dimension_mean) if fractal_dimension_mean else None
        
            radius_se = float(radius_se) if radius_se else None
            texture_se = float(texture_se) if texture_se else None
            perimeter_se = float(perimeter_se) if perimeter_se else None
            area_se = float(area_se) if area_se else None
            smoothness_se = float(smoothness_se) if smoothness_se else None
            compactness_se = float(compactness_se) if compactness_se else None
            concavity_se = float(concavity_se) if concavity_se else None
            concave_points_se = float(concave_points_se) if concave_points_se else None
            symmetry_se = float(symmetry_se) if symmetry_se else None
            fractal_dimension_se = float(fractal_dimension_se) if fractal_dimension_se else None
        
            radius_worst = float(radius_worst) if radius_worst else None
            texture_worst = float(texture_worst) if texture_worst else None
            perimeter_worst = float(perimeter_worst) if perimeter_worst else None
            area_worst = float(area_worst) if area_worst else None
            smoothness_worst = float(smoothness_worst) if smoothness_worst else None
            compactness_worst = float(compactness_worst) if compactness_worst else None
            concavity_worst = float(concavity_worst) if concavity_worst else None
            concave_points_worst = float(concave_points_worst) if concave_points_worst else None
            symmetry_worst = float(symmetry_worst) if symmetry_worst else None
            fractal_dimension_worst = float(fractal_dimension_worst) if fractal_dimension_worst else None
            
            # Predict using the machine learning model
            Breast_cancer_prediction = Breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean,
                                                                     area_mean, smoothness_mean, compactness_mean,
                                                                     concavity_mean, concave_points_mean, symmetry_mean,
                                                                     fractal_dimension_mean, radius_se, texture_se,
                                                                     perimeter_se, area_se, smoothness_se, compactness_se,
                                                                     concavity_se, concave_points_se, symmetry_se,
                                                                     fractal_dimension_se, radius_worst, texture_worst,
                                                                     perimeter_worst, area_worst, smoothness_worst,
                                                                     compactness_worst, concavity_worst, concave_points_worst,
                                                                     symmetry_worst, fractal_dimension_worst]])
            
            if Breast_cancer_prediction[0] == 1:
                Breast_cancer_diagnosis = "The Person has Breast Cancer disease"
            else:
                Breast_cancer_diagnosis = "The Person does not have Breast Cancer disease"
            
        except ValueError:
            Breast_cancer_diagnosis = "Invalid input. Please enter valid numeric values for all fields."
        
    st.success(Breast_cancer_diagnosis)
