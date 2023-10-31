import streamlit as st
import pandas as pd
import ydata_profiling as pp
import base64
import os
import openpyxl

st.set_page_config(page_title="Data Quality Profling Tool", page_icon='📈', layout="wide", initial_sidebar_state="expanded")

def main():
    data_file = st.file_uploader("Upload CSV or Excel File", type=['csv', 'xlsx'])
    if data_file is not None:
        file_extension = os.path.splitext(data_file.name)[1]
        if file_extension == '.csv':
            df = pd.read_csv(data_file)
        elif file_extension == '.xlsx':
            df = pd.read_excel(data_file, engine='openpyxl')

        st.subheader("Sample Data from File")
        st.dataframe(df.head())
        
        profile = pp.ProfileReport(df, title="Data Quality Profile Report", minimal=True)
        profile.to_file('profile_report.html')
        
        st.markdown(get_binary_file_downloader_html('profile_report.html', 'Data Quality Profile Report'), unsafe_allow_html=True)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<h3><a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">>>>Download {file_label}<<<</a></h3>'
    return href

if __name__ == '__main__':
    main()
