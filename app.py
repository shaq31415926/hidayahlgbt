import streamlit as st

st.title("Hi, Welcome to Hadiyah(). We are a voluntary organisation XXXX")

with st.chat_message("user"):
    st.write("Hello 👋 Are you based in the UK or US")
    uk = st.button("1. UK")
    us = st.button("2. US")
    international = st.button("3. International")

if international:
    st.write("Unfortunately we do not provide this info")

if uk or us:
    st.write("What type of resources are you looking for?")
    videos = st.button("Videos")
    podcasts = st.button("Podcasts")
    blogs = st.button("Blogs")
    organisation = st.button("Organisation")



