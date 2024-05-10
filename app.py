import streamlit as st
from clarifai.modules.css import ClarifaiStreamlitCSS

st.set_page_config(layout="wide")

import vocabulary_page  
import synonyms_page
import first_page
import translate

ClarifaiStreamlitCSS.insert_default_css(st)

# Tạo sidebar cho việc chọn trang
page = st.sidebar.selectbox('Choose your page', ['First Page', 'Vocabulary to Image','Synonym Generator','Translate'])

if  page == 'First Page':
    first_page.load_page()
elif page == 'Vocabulary to Image':
    vocabulary_page.load_page()
elif page == 'Synonym Generator':
    synonyms_page.load_page()
elif page == 'Translate':
    translate.load_page()
