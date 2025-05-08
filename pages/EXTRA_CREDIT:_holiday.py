import streamlit as st

st.markdown("<h1 style='text-align: center;'>EXTRA CREDIT: Favorite Holiday</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'><i>(A1 Rubric: Writing) </i>I can write intercultural journal entries with simple words and phrases about myself and my immediate environment.</h1>", unsafe_allow_html=True)

st.divider()

st.subheader("I'm writing about my favorite holiday: Diwali!, but as a diary entry.")

col1, col2 = st.columns(2)
with col1:
    st.image("images/diwali-celebration.jpg", width=400)

with col2:
    st.image("images/diwali-ninad.jpeg", width=400)

st.info('''
Hola,

Mi fiesta favorita es Diwali. Es una celebración muy especial en mi familia. En Diwali, encendemos muchas luces y velas. Mi familia y yo decoramos la casa con colores bonitos y flores. También comemos comida deliciosa como dulces y platos especiales. Me gusta mucho pasar tiempo con mi familia en este día. Usamos ropa nueva y hacemos fuegos artificiales por la noche. La casa está llena de luz y alegría.

Diwali es importante porque simboliza la victoria de la luz sobre la oscuridad. Me hace sentir feliz y cerca de mi cultura. También recibimos visitas de amigos y damos regalos pequeños. Escuchamos música tradicional y rezamos juntos. Es un día largo, pero muy bonito y divertido. Por eso, Diwali es mi fiesta favorita y espero siempre con emoción este día cada año.
''')