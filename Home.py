import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, empty_col1, col2 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Raghava Varanasi")

    content = """
        Hi, I am Raghava! I am a python programmer, a data scientist, machine learning and deep learning enthusiast.
        I graduated in the year 2019 with Master of Science in Mechanical Engineering from the Polytechnic University of
        Milan with my thesis in machine learning applications to understand the health and behavior of a structure under
        different conditions. This work has propelled my interests into the areas of AI. I did numerous projects in the
        machine learning, deep learning, and NLP applications. Feel free to check out my GitHub for looking at my projects.
    """

    st.info(content)

st.write('-'*20)
content2 = """Below you can find some of the apps I have built using python. Feel free to contact me!"""
st.write(content2)

data = pd.read_csv("data.csv", sep=";")
print(data.columns)
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])


for i in range(data.shape[0]):
    if i%2 != 0:
        with col3:
            st.subheader(data['title'][i])
            st.write(data['description'][i])
            st.image(f"images/{data['image'][i]}")
            st.write(f"[Source Code]({data['url'][i]})")

    elif i%2 == 0:
        with col4:
            st.subheader(data['title'][i])
            st.write(data['description'][i])
            st.image(f"images/{data['image'][i]}")
            st.write(f"[Source Code]({data['url'][i]})")

