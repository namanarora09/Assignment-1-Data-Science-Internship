# Importing Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
# absolute path of datase
DATA_PATH = os.path.join(dir_of_interest, "data", "fifa_eda_stats.csv")

st.title("Counting number of players from each country based on their overall score")

# importing the dataset
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

col1, col2 = st.columns(2)

# setting the values for the drop down menu
foot = col1.selectbox("Select the preferred foot", ["Left", "Right"])
score = col2.selectbox("Select the overall score range", [
    "Greater than 90", "Greater than 80", "Greater than 70", "Greater than 60", "Greater than 50", "less than or equal to 50"])

# calculating the required overall Score
overallScore = 0
if score == "Greater than 90":
    overallScore = 90
elif score == "Greater than 80":
    overallScore = 80
elif score == "Greater than 70":
    overallScore = 70
elif score == "Greater than 60":
    overallScore = 60
elif score == "Greater than 50":
    overallScore = 50

# Figure 1
fig_1 = px.histogram(
    df[df['Preferred Foot'] == foot], x="Nationality")
col1.plotly_chart(fig_1, use_container_width=True)

# Figure 2
fig_2 = px.histogram(
    df[df['Overall'] >= overallScore], x="Nationality")
col2.plotly_chart(fig_2, use_container_width=True)

st.caption("Created by Naman Arora")
