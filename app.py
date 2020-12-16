
# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import codecs
from pandas_profiling import ProfileReport 

# Components Pkgs
import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(page_title="Data Quality Profling Tool",page_icon='📈',layout="wide", initial_sidebar_state="expanded")
st.sidebar.header("Read Me")
st.sidebar.header("Help")
st.sidebar.text_area("Need help? Let us know.")
st.sidebar.button("Submit")
#st.sidebar.selectbox("asd",("a","b","c"))

def main():
  #st.header("Data Quality Profling Tool")
  data_file = st.file_uploader("Upload CSV or Excel File",type=['csv','xlsx'])
  
  if data_file is not None:
    try:
      df = pd.read_csv(data_file)
    except:
      df = pd.read_excel(data_file)
    st.subheader("Sample Data from File")
    st.dataframe(df.head())
    st.subheader("Data Quality Profile")
    profile = ProfileReport(df, minimal=True)
    filepath = st.text_input("Where do you want to save the report?")
    if filepath is not None:
      download = st.button("Download Report")
      if download:
        profile.to_file(filepath+"\Data Quality Profile.html")   
    st_profile_report(profile)
        

if __name__ == '__main__':
  main()
  hide_streamlit_style = """
  <style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
    </style>
  """
  st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
