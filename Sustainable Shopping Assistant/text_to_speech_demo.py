
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', 'english') 
engine.setProperty('rate', 150)

import streamlit as st
import pyttsx3

def my_program():
    engine.say("harish is a sunni")
    engine.runAndWait()
    # st.write("end")

st.write('This is my Streamlit app.')

if st.button('Run Program'):
    my_program()
    # my_program()