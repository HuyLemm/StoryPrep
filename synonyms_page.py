import streamlit as st
import requests
def set_text_input_color():
    # Custom CSS to change text input color
    css = """
    <style>
        input {
            color: black !important;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    

def get_synonyms(word):
    url = f"https://wordsapiv1.p.rapidapi.com/words/{word}/synonyms"
    headers = {
        "X-RapidAPI-Key": "c3da8005b6mshbec93b97ee9aa52p1a10c4jsn40255508d3c2",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('synonyms', [])
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
        return []

def load_page():
    st.title('Synonym Generator')
    set_text_input_color()
    # Nhập từ cần tìm từ đồng nghĩa
    word = st.text_input('Enter a word:', '')

    # Nút để tìm từ đồng nghĩa
    if st.button('Find Synonyms'):
        if word:
            synonyms = get_synonyms(word)
            if synonyms:
                st.write('Synonyms for {}:'.format(word))
                st.write(', '.join(synonyms))
            else:
                st.warning("No synonyms found for the given word.")
        else:
            st.warning("Please enter a word.")

# Chạy hàm load_page để tải trang
load_page()