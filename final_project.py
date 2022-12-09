import pandas as pd
#pip install pandas openpyxl
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Emoji collection page: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Mini Online Vet", page_icon=":crystall_ball:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---CSS STYLING FILE---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style_fp/style.css")

# ---LOAD ASSETS---
# use lottiefil
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_g8jizdgx.json")
image_temp = Image.open("images_fp/temp.jpg")

# -----HEADR SECTION-----
with st.container():
    st.subheader("Hi, My name is Huiqin :eyes:")
    st.title("Peeka and Guava's mom")
    st.write("I adopted Peeka and Guava three months ago")
    st.write("[Our Instagram Page:sparkling_heart:>](https://www.instagram.com/peekaandguava)")


# ----PROJECT PURPOSE----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Why I am building this website")
        st.write("##")
        st.write(
            """
            Ever since I adopted my cats three months ago, I have been visiting the vet at least twice a month. \n
            There is a severe shortage of vet across the U.S. right now\n
            And I noticed it's very hard to find vets and cat hospitals in the SF area\n
            So I want to build a website that could:
            - find cat hospitals / vet clinics based on your district
            - find the closet cat hospital based on your coordinates
            """)
    with right_column:
        st_lottie(lottie_coding, height=600, key="meow")


# ---Vet Locator---
with st.container():
    st.write("---")
    st.header("Vet Locators")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image_temp)
    with text_column:
        st.subheader("Find pet hospitals based on your district")
        st.write(
            """
            Use this one to find pet hospitals based on your district!\n
            Just select your district from the drop down bar\n
            And the website will show you the pet hospitals in your district!
            """)
        st.markdown("[Click here...](https.//google.com)")


# --- ACTUAL LOCATOR ---
with st.container():
    st.header("Vet Locator")
    district_list = ["SOMA", "Daly City", "Chinatown"]

    st.header("Please select")
    district_selected = st.selectbox("Which neighborhood do you live in?",
                                     options = district_list)





# --- CONTACT FORM ---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Website used: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/hu.huiq@northeastern.edu" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


#for the map, tuple(x, y), name of the vet clinic
#one to search nearest vet by
