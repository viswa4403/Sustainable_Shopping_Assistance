import streamlit as st
import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Define the Streamlit app
def app():
    st.title("Voice Recognition Chatbot")
    
    # Add a button to start the recognition
    if st.button("Start Recording"):
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            st.info("Listening...")
            # Adjust the recognizer for ambient noise
            r.adjust_for_ambient_noise(source)
            # Record the audio
            audio = r.listen(source)
            st.success("Recording Complete!")
            
            # Use Google Speech Recognition to transcribe the audio
            try:
                text = r.recognize_google(audio)
                st.write(f"You said: {text}")
            except sr.UnknownValueError:
                st.warning("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                st.error(f"Could not request results from Google Speech Recognition service; {e}")
app()