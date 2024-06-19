import os, random
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_clickable_images import clickable_images
from st_pages import Page, show_pages, hide_pages
from pyunsplash import PyUnsplash
from dotenv import load_dotenv
     
show_pages(
    [
        Page("GraphicalPass.py", "Home", "🏠"),
        Page("pages/0_Testing.py", "TestPage", "🚧"),
        Page("pages/1_PassImg.py", "PassImg", "🖼️"),
        Page("pages/2_PathPass.py", "PathPass", "📸"),
        Page("pages/8_MyDSM_v6.py", "MyDSM_v6", "🎮"),
        Page("pages/9_StoryBoard2.py", "StoryBoard2", "🎮"),
        Page("pages/11_StoryBoard4.py", "StoryBoard4", "🎮"),
        Page("pages/12_StoryBoard5.py", "StoryBoard5", "🎮"),
        Page("pages/13_WIP.py", "WIP", "🎮"),
        Page("pages/login_PassImg.py", "Login_Splash", "🖥️"),
        Page("pages/AccessDenied.py", "AccessDenied", "❌")
    ]
)

# Login Splash and Access Denied pages are hidden.
hide_pages(
    [
        "login splash", "login PassImg", "login passimg", "login_passimg", "login_PassImg", "login_splash", "Login Splash", "Login_Splash", "AccessDenied", "accessdenied"
    ]
)

# --------------------------------------------------------------
# PREAMBLE
sess_grid = (
    [
        "https://images.unsplash.com/photo-1613336026275-d6d473084e85?w=700", # pass-img 1: Coffee
        "https://images.unsplash.com/photo-1503792070985-b4147d061915?w=700", # pass-img 2: Key
        "https://images.unsplash.com/photo-1552841847-0e031d33a283?w=700" # pass-img 3: Lemon slices
    ]
)


# Tuples
one = ("Q", "A", "Z")
two = ("W", "S", "X")
three = ("E", "D", "C")
four = ("R", "F", "V")
five = ("T", "G", "B")
six = ("Y", "H", "N")
seven = ("U", "J", "M")
eight = ("I", "K")
nine = ("O", "L")
zero = ("P",) # Make sure to put comma at the end if single variable to indicate tuple

kbd2num = [one, two, three, four, five, six, seven, eight, nine, zero]

# Loading the environment files
load_dotenv()
pu = PyUnsplash(api_key=os.getenv('SB3_API'))

# Other file preamble
a2z = "ABCDEFGHIKLMNOPQRSTUVWYZ" # X taken out
alph_list = list(a2z) # I put this here just for the widget keys
default_val = None
state = st.session_state
#pw2num = []

# --------------------------------------------------------------
# FUNCTIONS
def unsplash_gen(Photo_Q, sess_img_grid):
    photo_atts = []
    #Photo_Q = "coffee"
    photos = pu.photos(type_='random', count=22, featured=True, query=Photo_Q)
    for photo in photos.entries:
        sess_img_grid.append(photo.link_download)
        photo_atts.append(photo.get_attribution(format="txt"))


def create_img(sess_img_grid, index, pwlist):

    clicked = clickable_images(
    paths = sess_img_grid[index-1:index], # grid generation happens at session_state below
    titles=["Image #" + str(index)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
    key=alph_list[index-1:index]
    )

    if (sess_img_grid[index-1:index] == ['https://images.unsplash.com/photo-1613336026275-d6d473084e85?w=700']):
        pwlist.append(index)
    elif (sess_img_grid[index-1:index] == ['https://images.unsplash.com/photo-1503792070985-b4147d061915?w=700']):
        pwlist.append(index)
    elif (sess_img_grid[index-1:index] == ['https://images.unsplash.com/photo-1552841847-0e031d33a283?w=700']):
        pwlist.append(index)

    return pwlist


def create_grid(sess_img_grid):
    st.write(" # WIP System Login")

    c1, c2, c3, c4, c5 = st.columns(5) # creates 5 columns side by side
    pw1 = []
    pw2num = []
    str2int = []
    index2alph = []

    with c1:
        for index in range(1, 6):
            pw1 = create_img(sess_img_grid, index, pw1)
            #if p1 is not None:
                #pw1.append(p1)
            
    with c2:
        for index in range(6, 11):
            pw1 = create_img(sess_img_grid, index, pw1)
            #if p1 is not None:
                #pw1.append(p1)

    with c3:
        for index in range(11, 16):
            pw1 = create_img(sess_img_grid, index, pw1)
            #if p1 is not None:
                #pw1.append(p1)

    with c4:
        for index in range(16, 21):
            pw1 = create_img(sess_img_grid, index, pw1)
            #if p1 is not None:
                #pw1.append(p1)

    with c5:
        for index in range(21, 26):
            pw1 = create_img(sess_img_grid, index, pw1)
            #if p1 is not None:
                #pw1.append(p1)

    print(f"PW1 Indexes = ",pw1)
    for i in range(len(pw1)):
        index2alph.append(alph_list[pw1[i]-1])
    print(f"PW1 Index2Alph = ",index2alph)

    for i in range(len(index2alph)):
        for j in range(len(kbd2num)):
            if(index2alph[i] in kbd2num[j]):
                #print(j+1) # This part takes the number as an integer
                pw2num.append(j+1)
    pw2num.sort()

    x = st.text_input("Enter Key", value=default_val, key="value")
    st.write(x)
    if x is not None:
        pw_unpack = [*x]

        for s in pw_unpack:
            str2int.append(int(s))
        str2int.sort()

    


    if (input is not None) and str2int == pw2num:
        switch_page("login splash")
    elif(input is not None) and (str2int != pw2num):
        st.write("Access Denied!")
        #switch_page("AccessDenied")






# ---------------------------------------------------------------
# CALLING FUNCTIONS
unsplash_gen("random", sess_grid)


# ----------------------------------------------------------------
# RUNNING THE MAIN CODE
class main:
    # Initialises the session variable for the current user session
    def __init__(self):
        if "sb_img_grid" not in st.session_state:
            st.session_state["sb_img_grid"] = random.sample(sess_grid,25) # this is where the grid is actually generated
        self.sb_img_grid = st.session_state["sb_img_grid"] # have to change the name with each app
        self.run()

    # This part actually runs the main code
    def run(self):
        create_grid(st.session_state["sb_img_grid"])

if __name__ == '__main__':
    main()


