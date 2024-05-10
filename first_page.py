import streamlit as st
import streamlit.components.v1 as components
import os

def load_page():

    with open(r'C:\Users\lthuy\Documents\XuLyNgonNguTuNhien\module-story-prep\style.css') as f:  
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Application.
    api_key = os.environ.get('CLARIFAI_PAT', '7be6e68329d74c789a7f3057b740ec0b')
    components.iframe(f"https://storyprep.vercel.app/?api_key={api_key}", scrolling=True)
