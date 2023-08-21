
import streamlit as st
import pandas as pd
from mitosheet.streamlit.v1 import spreadsheet


st.set_page_config(layout="wide")
st.title("Data Cleaning Verification")


dfs, _ = spreadsheet(import_folder='./data')

