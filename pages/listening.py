import streamlit as st

st.markdown("<h1 style='text-align: center;'>Listening</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'><i>(A1 Rubric: Listening)</i> I can understand simple questions about myself, days of the week,"
             "months, clock times and dates and names of everyday objects.</h1>", unsafe_allow_html=True)
st.divider()
st.subheader("I listen to this video every few days to gain familiarity with the most commonly used words in conversations.")
st.video("https://youtu.be/Xo5Y7AHMy20?feature=shared")
st.info("Now, I know what a few more words are. For example, look is mirar and way is el camino.")


st.divider()

st.subheader("I watch vlogs like this one to be able to understand Spanish when it is used in a conversation with me.")
st.video("https://youtu.be/3nb_hjv5Y24?feature=shared")
st.info("Now, I know what a few everyday activities are called and how objects are used.")
