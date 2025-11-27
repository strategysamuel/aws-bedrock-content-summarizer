import streamlit as st
import text_lib as glib

st.set_page_config(page_title="Text Summarizer")
st.title("Text Summarizer (Amazon Bedrock + Streamlit)")

input_text = st.text_area("Paste your content here", label_visibility="collapsed")
go_button = st.button("Summarize", type="primary")

if go_button and input_text.strip():
    with st.spinner("Summarizing..."):
        summary = glib.get_text_response(input_content=input_text)
        st.subheader("Summary")
        st.write(summary)
