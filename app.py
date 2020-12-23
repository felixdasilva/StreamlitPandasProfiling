
# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import codecs
import pandas_profiling as pp
import base64
import os
#from pandas_profiling import ProfileReport 

# Components Pkgs
import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report
import openpyxl

#Page Setup
st.set_page_config(page_title="Data Quality Profling Tool",page_icon='📈',layout="wide", initial_sidebar_state="expanded")

def main():
  #st.header("Data Quality Profling Tool")
  data_file = st.file_uploader("Upload CSV or Excel File",type=['csv','xlsx'])
  
  if data_file is not None:
    try:
      df = pd.read_csv(data_file)
    except:
      df = pd.read_excel(data_file, engine='openpyxl')
    st.subheader("Sample Data from File")
    st.dataframe(df.head())
    #st.subheader("Data Quality Profile")
    profile = pp.ProfileReport(df, minimal=True)
    profile.to_file('profile_report.html')
    #filepath = st.text_input("Where do you want to save the report?")
    #if filepath is not None:
      #download = st.button("Download Report")
      #if download:
        #profile.to_file(filepath+"\Data Quality Profile.html")   
    #st_profile_report(profile)
    
#Download File Command
    with open('profile_report.html', 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<h3><a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename('profile_report.html')}">Download Data Quality Profile Report</a></h3>'

#def get_binary_file_downloader_html(bin_file, file_label='File'):
#    with open(bin_file, 'rb') as f:
#        data = f.read()
#    bin_str = base64.b64encode(data).decode()
#    href = f'<h3><a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a></h3>'
#    return href
        

if __name__ == '__main__':
  main()
  hide_streamlit_style = """
  <style>
  MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  </style>
  """
  st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
#  st.markdown(get_binary_file_downloader_html('profile_report.html', 'Data Quality Profile Report'), unsafe_allow_html=True)
