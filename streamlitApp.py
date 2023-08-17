import streamlit as st
import time as t
#title- used to add the title of an app
st.title("Welcome here buddy!!")
#header
st.header("Machine Learning")

st.subheader("Linear Regression")
st.info("I am CHIRAG CHAUHAN (DEVELOPER)")
st.warning("Enjoy Life DEAR!!")
st.write("World is a single Conciousness")
st.error("Wrong Password")
st.success("CONGRATULATIONS!!")
st.markdown("# mark1")
st.markdown("## mark2")
st.markdown("### mark3")
st.markdown(":cat:")
st.text("I love Artificial Intelligence!")
st.caption("Caption is Here")
st.latex(r'''a+b x^2+c''')

st.checkbox("Login")
st.button("Click if you are not GAY!:car:")

st.radio("Pick your gender",["MALE","FEMALE","MENTALLY UNSTABLE PSYCHOPATH"])

st.image("drinker.png")
st.selectbox("Pick your course",["MACHINE LEARNING","CLOUD COMPUTING","CYBER SECURITY"])
st.multiselect("Pick your course",["MACHINE LEARNING","CLOUD COMPUTING","CYBER SECURITY"])
st.select_slider("Rating",["Bad","Good","Outstanding"])
st.slider("Enter your number:",0,100)

st.number_input("Pick a Number",0,100)
st.text_input("Enter your Email address:email:")
st.date_input("Opening ceremony:date:")
st.time_input("What's the time:")
st.text_area("Tell us about yourself!")
st.file_uploader("upload your documents")
st.color_picker("color")
st.progress(90)

with st.spinner("Just Wait"):
    t.sleep(2)
    
st.balloons()
st.sidebar.title("Welcome Page")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("Password")

import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
