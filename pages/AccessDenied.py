import os #,cv2
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
import extra_streamlit_components as stx
#from streamlit_extras.altex import line_chart, get_stocks_data
from st_pages import Page, show_pages, hide_pages

st.set_page_config(
    page_title="Access Denied",
    page_icon="❌",
)

show_pages(
    [
        Page("GraphicalPass.py", "Home", "🏠"),
        Page("pages/1_WIP.py", "WIP", "🎮"),
        Page("pages/login_PassImg.py", "Login_Splash", "🖥️"),
        Page("pages/AccessDenied.py", "AccessDenied", "❌")
    ]
)

# Make sure to hide login splash!!
hide_pages(
    [
        "login splash", "login PassImg", "login passimg", "login_passimg", "login_PassImg", "login_splash", "Login Splash", "Login_Splash"
    ]
)

st.session_state["Count"] = 0
st.write("# Access Denied!")



# Codes when kill terminal

# .\graph_app\Scripts\activate
# cd raw_code
# streamlit run GraphicalPass.py