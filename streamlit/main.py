import requests
import streamlit as st
import requests as r
from scripts import helpers

config = helpers.get_config()

# sidebar
st.sidebar.header('Information')


st.sidebar.header('Configuration')

side_crop_text = st.sidebar.subheader('Selection of inference method')
side_crop_selection = st.sidebar.selectbox('Mode',
                                           ('Mocked', 'Google Cloud Services'))

# main
st.header('Automatic Detection of Faces in Images')
st.text('Depending on the selected mode a face detection is run on the input image.'
        '\nIf Mode "Mocked" is selected a default value is returned')

st.subheader('Image Upload')

global file
file = st.file_uploader(label="Place an image file in the box below", type=["png", "jpg", "jpeg"])

if st.button('Run face detection'):
    if file is not None:
        payload = {}
        headers = {}

        response = requests.request("POST", config['FASTAPI_URL'], headers=headers, data=payload)
    else:
        st.warning("Please upload an image first")
