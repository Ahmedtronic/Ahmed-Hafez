import streamlit as st
from st_functions import st_button, load_css
from PIL import Image
st.set_page_config(page_title="Ahmed Hafez portfolio",layout="centered")
load_css()
st.write("[![Watch](https://komarev.com/ghpvc/?username=Ahmedtronic&label=Profile%20views&color=0e75b6&style=flat)](https://gitHub.com/Ahmedtronic)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('pp.png'))

st.header('''Ahmed Hafez Abd El Fatah 
AI Engineer | Problem Solver | INFJ.''')

st.info('''AI Engineer with concrete background in mathematics and problem solving and the ability to innovate, apply and integrate AI-based solutions in multiple fields such as Embedded system, Medical field and Software Engineering. 

5 times ECPC participant, Tedx speaker and more… 

In Real Life: 

A Dreamer Who Always Believes That It's All About The Journey and That Our True Value Is What We Give to, Not What We Take From.''')

icon_size = 20
cv="/Ahmed_Hafez_CV_4.pdf"

st_button('youtube', 'https://youtube.com/@aitronix8705', 'Aitronix YouTube channel', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/ahmedtronic/', 'LinkedIn', icon_size)
st_button('twitter', 'https://twitter.com/Ahmedtronic', 'Twitter', icon_size)
st_button('github', 'https://github.com/ahmedtronic', 'Github', icon_size)
st_button('', 'https://codeforces.com/profile/Ahmedtronic', 'Codeforces', icon_size)
st_button('', 'https://www.kaggle.com/ahmedtronic', 'Kaggle', icon_size)

with open(cv[1:], "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download My Cv",data=PDFbyte,file_name="Ahmed_Hafez_CV_4.pdf",mime='application/octet-stream')