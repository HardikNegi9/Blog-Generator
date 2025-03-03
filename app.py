import streamlit as st
from graph import generate_markdown
from IPython.display import Markdown


st.title("Blog Generator")

title = st.text_input("Enter the title:")
if st.button("Generate"):
    if title:
        markdown_output = generate_markdown(title)
        st.markdown(markdown_output)
    else:
        st.error("Please enter a title.")