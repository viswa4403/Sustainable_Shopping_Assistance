import streamlit as st
#import pyttsx3
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv
load_dotenv()
import openai
import speech_recognition as sr

#text to speech
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', 'english') 
engine.setProperty('rate', 150)
#end

openai.api_key = "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"
st.title("Chatbot : Eco-Friendly Shopping Assistant")
st.subheader("AI Tutor:")

# model = st.selectbox(
#     "Select a model",
#     ("gpt-3.5-turbo", "gpt-4")
# )

# def speech_To_Text():
#     r = sr.Recognizer()

#     # Start recording audio from the microphone
#     with sr.Microphone() as source:
#         st.write("Say something!")
#         audio = r.listen(source)

#     # Recognize speech using Google Speech Recognition
#     try:
#         st.write("You said: " + r.recognize_google(audio))
#         query = r.recognize_google(audio)
#     except sr.UnknownValueError:
#         st.write("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         st.write(
#             "Could not request results from Google Speech Recognition service; {0}".format(e))
        
#     return query

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []


#
query = st.text_input("Query: ", key="input")

# if st.button("press here to talk"):
#     #cALL voice
#     query = speech_To_Text()
#


prompt = """
  Alternatives for {0} which is eco friendly

    It should be in this format:
    The alternative :positive  impact of this on the environment
    give exactly 3 alternatives
    avoid any other additional details
    be precise with your details
""".format(query)

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()
if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", prompt )
        response = get_chatgpt_response(messages, "gpt-3.5-turbo")
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)
if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
        engine.say(response)
    engine.runAndWait()