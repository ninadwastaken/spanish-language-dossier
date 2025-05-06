import pandas as pd
import streamlit as st
import csv
import pandas


st.set_page_config(layout='wide')
st.markdown("<h1 style='text-align: center;'>Ninad's Spanish Dossier!!!</h1>", unsafe_allow_html=True)

st.divider()


col1,col2 = st.columns(2)

with col1:
    st.image("images/ninad.jpeg", width=400)

with col2:
    st.header('''
    ¡Hola! Me llamo Ninad Moharir. I’m a sophomore at the NYU Tandon School of Engineering majoring in Computer Science. This dossier outlines the progress I’ve made learning Spanish, in particular through Elementary Spanish 1 in NYUAD in Spring 2025. I am a native English and Hindi speaker. I decided to start learning Spanish to be able to communicate with my Hispanic friends, and learn more about this beautiful culture.''')

st.divider()

st.header("Highlights")
st.table(pd.DataFrame({
    "Works": ["Language Passport", "Peer Tutoring Sessions", "Midterm Exam", "Final Dossier & Video"],
    "Date": ["January 2025", "January-May 2025", "March 2025", "May 2025"],
    "Skill Level": ["A1", "A1", "A1", "A1"]
}))

st.divider()

st.header("Future Goals")
st.info("I want to be fluent in Spanish to the point that my ethnicity gets questioned. To do so, I will take more Spanish classes"
        "and indulge in more conversations with native speakers. In addition, I plan on travelling the Americas, which will bolster"
        "my Spanish and my understanding of the diverse cultures of the region.")
st.info("I want to thank Professor Eduardo Lage-Otero, and my peer tutor Silvana for helping me get to this stage "
        "in my Spanish journey. I hope to make you proud in the future!")


