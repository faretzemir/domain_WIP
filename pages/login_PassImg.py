import os #,cv2
import streamlit as st
#import extra_streamlit_components as stx
from st_pages import Page, show_pages, hide_pages
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Login Splash",
    page_icon="🖥️",
)

show_pages(
    [
        Page("GraphicalPass.py", "Home", "🏠"),
        Page("pages/1_WIP.py", "WIP", "🎮"),
        Page("pages/login_PassImg.py", "Login_Splash", "🖥️"),
        Page("pages/AccessDenied.py", "AccessDenied", "❌")
    ]
)

IMG_PATH = "img/bnm.png"
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["USD", "GBP", "CHF"])



st.image(IMG_PATH)
#st.title("Bank of Malaysia")
st.divider()
st.subheader("Welcome to the Homepage of the Bank of Malaysia.")
st.write("Comparison of live currency exchange values.")

st.line_chart(chart_data)




# Codes when kill terminal

# .\graph_app\Scripts\activate
# cd raw_code
# streamlit run GraphicalPass.py