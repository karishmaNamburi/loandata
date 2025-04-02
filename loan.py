import streamlit as st
import joblib
st.title('Loan Approval process Automation')
model=joblib.load("loan_data1.joblib")
Gender=st.number_input('enter gender Male:0,Female:1')
Married=st.number_input('enter martial status Married:0,Unmarried:1')
Income=st.number_input('enter the applicant income in thousands')
la=st.number_input('enter the loan amount in thousands')
if st.button('Predict Approval'):
    Prediction=model.predict([[Gender,Married,Income,la]])
    if Prediction=='y':
        st.txt('Loan Approved')
    else:
        st.txt('Loan Rejected')
