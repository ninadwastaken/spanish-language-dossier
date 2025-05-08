import streamlit as st

st.markdown("<h1 style='text-align: center;'>Reading</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'><i>(A1 Rubric: Reading) </i>I can read and understand materials "
            "that contain basic vocabulary related to personal details such as name, address, age, etc.</h1>",
            unsafe_allow_html=True)

st.divider()

st.subheader("I filled out forms in Spanish.")
st.link_button(label="Form 1", url="https://www.jotform.com/form-templates/spanish-staff-self-evaluation")
st.link_button(label="Form 2", url="https://www.jotform.com/form-templates/celmi")
st.link_button(label="Form 3", url="https://www.elespanol.com/el-cultural/suscripciones/")
st.info('''
Recently, I practiced filling out simple forms in Spanish online, which helped me learn useful vocabulary about personal details. I saw words like Nombre (name), Apellido (last name), Dirección (address), and Teléfono (phone number), which appear in many sign-up forms. It was interesting to see that even common buttons had phrases like continuar con Google (continue with Google) and crear mi cuenta (create my account). Seeing these words in context made it easier for me to remember them.

I also learned that Correo electrónico means email address, and Contraseña is password. Now, when I see these words on Spanish websites, I feel more confident that I understand what to do. Filling out the forms felt like a small but practical way to practice reading in Spanish, and it showed me that I can already understand more than I thought when it comes to everyday tasks like making an account or signing up for a newsletter.
''')

col1, col2 = st.columns(2)
with col1:
    st.image("images/spanish_form_1.png")
with col2:
    st.image("images/spanish_form_2.png")