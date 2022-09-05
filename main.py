import streamlit as st
import pickle
pickle_in=open('SalaryPrediction .pkl','rb')
model=pickle.load(pickle_in)

years=st.number_input('Years of Experience')
if st.button('PREDICT'):
  salary=model.predict([[years]])
  st.success(f'SALARY PREDICTED IS {salary}')
