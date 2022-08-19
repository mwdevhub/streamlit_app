import streamlit as st


def fun():
    st.write('SNOW')
    st.snow()
    return


st.write("""
    # My first app
    The snow *button!*""")


if st.button('Click for snow'):
    fun()
