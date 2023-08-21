import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet
import pandas as pd
from io import StringIO
import os

st.set_page_config(layout="wide")
st.title('Demo app using for EDA')
from tempfile import NamedTemporaryFile

file = st.text_input('Enter file directory')

if file:
    st.write(file)
    spreadsheet(import_folder=file)
# uploaded_file = st.file_uploader(label="Select your file for analysis",type='csv')
# # # file_location =
# # # file_location =  os. getcwd()
# if uploaded_file is not None:
#     with NamedTemporaryFile(dir='.', suffix='.csv') as f:
#         # f.write(uploaded_file.getbuffer())
#         file_location = f.name
#         file_dir = os.path.dirname(file_location)
#         st.write(file_location)
#         st.write(file_dir)
#         file_contents = uploaded_file.read()

        # st.write(file_contents)
        # st.write(file_contents)
        # df = pd.DataFrame(file_contents)
        # print(df)
        # st.dataframe(data=pd.DataFrame(file_contents))
    # dataframe = pd.read_csv(uploaded_file)
    # df1, code = spreadsheet(import_folder=file_location,df_names='df1')
    # st.write(uploaded_file)
#     # st.code(code)
