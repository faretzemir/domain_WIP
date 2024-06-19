import os #,cv2
import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
#import extra_streamlit_components as stx
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages
#from dotenv import load_dotenv
from pathlib import Path

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

# All available pages must be shown, otherwise, the page manager does not understand.
# Subsequent confidential or sensitive pages can be hidden using a function.

show_pages(
    [
        Page("GraphicalPass.py", "Home", "🏠"),
        Page("pages/13_WIP.py", "WIP", "🎮"),
        Page("pages/login_PassImg.py", "Login_Splash", "🖥️"),
        Page("pages/AccessDenied.py", "AccessDenied", "❌")
    ]
)

# Login Splash and Access Denied pages are hidden.
# This is done via CSS but have to be secure for final product!
hide_pages(
    [
        "login splash", "login PassImg", "login passimg", "login_passimg", "login_PassImg", "login_splash", "Login Splash", "Login_Splash", "AccessDenied", "accessdenied"
    ]
)

#load_dotenv()
#dotenv_path = Path('/env')

st.write("# Welcome to Graphical Passwords!")

st.sidebar.success("Select a system from the list.")

st.markdown(
    """
   This project was made entirely using **Streamlit**.
    
    Faretz Emir Imran (1171100781)\n
    **Made in partial fulfilment for Masters of Engineering Science**.

    Supervisor: Assoc. Prof. Ir. Dr. Goh Vik Tor\n
"""
)

#router = init_router()
#router.show_route_view()

# Codes when kill terminal

# .\graph_app\Scripts\activate
# cd raw_code
# streamlit run GraphicalPass.py