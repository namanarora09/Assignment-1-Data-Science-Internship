import streamlit as st
from matplotlib import image

st.title(":red[Welcome] to Assignment 1 of Data Science Internship")
st.header("I have used the football dataset for creating data visualization.")

st.header("Who do you think is better??")
st.subheader("Please do answer")

btn1 = st.button("Leonel Messi")
btn2 = st.button("Christiano Ronaldo")

if btn1 == True:
    st.warning("Please try another option", icon="⚠️")

if btn2 == True:
    img = image.imread("resources\images\Football_image.webp")
    st.success("Perfect Choice")
    st.image(img)
    st.balloons()

st.caption("Created by Naman Arora")
