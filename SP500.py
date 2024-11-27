import streamlit as st
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
data = pd.DataFrame(np.random.randn(50,2), columns = ['Age','BMI'])
st.sidebar.write("Select a Sector-Specific ETF")
selected_option = st.sidebar.radio("Select any option", options= ('XLC for Communication Services', 'XLY for Consumer Discretionary', 'XLP for Consumer Staples', 'XLE for Energy', 'XLF for Financials', 'XLV for Health Care', 'XLI for Industrials', 'XLK for Information Technology', 'XLB for Materials', 'XLRE for Real Estate', 'XLU for Utilities',))
                                   
if selected_option=='Line':
    st.line_chart(data)
elif selected_option=='Bar':
    st.bar_chart(data)
else:
    st.area_chart(data)