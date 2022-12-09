import pandas as pd
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Emoji collection page: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Mini Online Vet", page_icon=":crystall_ball:")

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
    st.subheader("Hi, My name is Huiqin")
    st.title("Peeka and Guava's mom :sparkles:")
    st.write("I adopted Peeka and Guava three months ago")
    st.write("[Our Instagram Page:sparkling_heart:>](https://www.instagram.com/peekaandguava)")


# ----PROJECT PURPOSE----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Why I am building this website:grey_question:")
        st.write("##")
        st.write(
            """
            Ever since I adopted my cats, I have been visiting the vet at least twice a month. \n
            It's very easy for small cats to get sick \n
            But there is a severe shortage of vet across the U.S. right now\n
            And I noticed it's very hard to find vets and cat hospitals in the SF area\n
            """)
    with right_column:
        st_lottie(lottie_coding, height=600, key="meow")


# ---Vet Locator---
with st.container():
    st.write("---")
    st.header("My Solution! :key:")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image_temp)
    with text_column:
        st.write(
            """
            I decided to build a website that could:
            - find cat hospitals / vet clinics based on your district
            - find cat hospital based on your zip code
            Use this one to find pet hospitals based on your district!\n
            Just select your district and ZIP code from the drop down bar\n
            And the website will show you the pet hospitals in your district!\n
            The list includes mostly hospitals in the SF area\n
            For emergency hospitals in the bay area\m
            Please click the link below to see an Emergency Hospital Referral List compiled by SF SPCA :gift_heart:
            """)
        st.markdown("[Referral List by SF SPCA](https://www.sfspca.org/wp-content/uploads/2022/05/ESHoursMission_referralList_8.5x11-05.05.22_final5.pdf)")


# --- ACTUAL LOCATOR ---
with st.container():
    st.header("Vet Locator :hospital:")
    district_list = ["SOMA", "Daly City", "Chinatown"]


    # import Excel file
    datafile = pd.read_excel(
        io='cat_hospital.xlsx',
        engine='openpyxl',
        sheet_name='Sheet1',
        skiprows=0,
        usecols='A:F',
        nrows=25,
    )


    st.subheader("Let's try to find some hospitals in your neighborhood")
    district = st.selectbox("Which neighborhood do you live in?",
                                     options=datafile["Neighborhood"].unique())
    datafile_bydistrict = datafile.query(
        "Neighborhood == @district"
    )
    st.dataframe(datafile_bydistrict)

    st.subheader("Now let's try to find them by your zip code!")
    zip_selected = st.selectbox("What's your zipcode?",
                                     options=datafile["ZIP_Code"].unique())

    datafile_byzip = datafile.query(
        "ZIP_Code == @zip_selected"
    )
    st.dataframe(datafile_byzip)


# --- CONTACT FORM ---
with st.container():
    st.write("---")
    st.subheader("If you have any questions, or would like to contribute more hospitals to the list,\n")
    st.subheader("Please don't hesitate to get in touch with me!")
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
