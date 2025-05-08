import streamlit as st

st.markdown("<h1 style='text-align: center;'>Writing</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'><i>(A1 Rubric: Writing) </i> I can identify and copy relevant copy words "
            "and phrases, e.g. from a diagram or set of instructions</h1>", unsafe_allow_html=True)

st.divider()

st.subheader("I sent an email to help my Hispanic friend cook an Indian dish: Vada Pav.")

col1, col2 = st.columns(2)
with col1:
    st.image("images/vada_pav.jpeg", width=400)

with col2:
    st.image("images/vada_pav2.jpeg", width=400)

st.info('''
Hola Angel,

¿Cómo estás? Quiero contarte sobre un plato indio muy popular. Se llama Vada Pav. Es fácil de hacer y muy sabroso.

Necesitas:

-Patatas

-Panecillos (pan de pav)

-Ajo

-Guindilla (chile picante)

-Harina de garbanzo

-Especias

-Aceite



Pasos:

-Cocina las patatas y aplástalas con ajo, guindilla y especias.

-Forma bolitas con la mezcla.

-Cúbrelas con harina de garbanzo y fríelas en aceite.

-Sirve dentro del panecillo con chutney picante.

-Es muy delicioso. ¡Pruébalo!


Un abrazo,

Ninad
''')

