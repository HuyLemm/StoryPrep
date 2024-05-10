import streamlit as st
from googletrans import Translator

def set_text_input_color():
    # Custom CSS to change text input color
    css = """
    <style>
        textarea {
            color: black !important;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)
    return translated_text.text

def load_page():
    st.title('Translation')
    set_text_input_color()  # Set color for text input
    input_text = st.text_area("Enter text to translate", "", height=300)
    if st.button("Translate"):
        if input_text:
            translated_text = translate_text(input_text, "en", "vi")
            st.write(f"Translated to Vietnamese: {translated_text}")
        else:
            st.warning("Please enter your text to translate.")

load_page()
