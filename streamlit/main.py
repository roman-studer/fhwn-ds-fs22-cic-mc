import requests
import streamlit as st
import requests
import sys

sys.path.insert(0, '../scripts/')
from helpers import get_config

config = get_config()

# sidebar
st.sidebar.header('Information')
side_information_text = st.sidebar.write('This application has been created to test and demonstrate the required functionality for the mini-challenge in the module Cloud Infrastructure and Computing. \
                      After an image has been uploaded and the right mode is selected, the image will be sent to a FastAPI, which in return is connected to Google Cloud Services. \
                      If Mode is "Mocked" a default response will be returned. Else a face detection will be performed on the input image.')

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

        response = requests.request("POST", config['FASTAPI_URL'] + '/predict', headers=headers, data=payload)
    else:
        st.warning("Please upload an image first")
