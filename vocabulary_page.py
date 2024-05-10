import streamlit as st
import requests
import json

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


    
def load_page():
    st.title('Image Generator from Pexels')
    set_text_input_color()
    # Yêu cầu người dùng nhập từ khóa
    query = st.text_input('Enter a search term:', '')

    # Nút để tìm kiếm và hiển thị hình ảnh
    if st.button('Search Images'):
        if query:
            images = search_images(query)
            if images:
                for img in images:
                    st.image(img['src']['original'], use_column_width=True, caption=query)
            else:
                st.error("No images found.")
        else:
            st.warning("Please enter a search term.")

def search_images(query):
    api_key = 'MapS9ABwPP4N6ANYVvfvHA3bUFJd9vmJAnRRWDqtidXcguRiEYOz7coi'
    url = 'https://api.pexels.com/v1/search'
    headers = {
        'Authorization': api_key
    }
    params = {
        'query': query,
        'per_page': 1
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        photos = response.json().get('photos', [])
        return photos
    else:
        st.error(f"Failed to generate image: {response.status_code}, {response.text}")
        return None

load_page()
