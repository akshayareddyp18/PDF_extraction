import streamlit as st
import json
from pdf_outline_extractor import extract_outline

st.set_page_config(page_title="PDF Outline Extractor", layout="centered")

st.title("📘 PDF Outline Extractor")
st.caption("Upload a PDF and extract its structured outline (Title, H1, H2, H3)")

uploaded_pdf = st.file_uploader("📤 Upload your PDF", type=["pdf"])

if uploaded_pdf:
    with st.spinner("⏳ Extracting outline..."):
        result = extract_outline(uploaded_pdf)

        st.success("✅ Outline extracted!")
        st.json(result)

        # Download button
        st.download_button(
            label="📥 Download JSON",
            data=json.dumps(result, indent=2),
            file_name=f"{uploaded_pdf.name.replace('.pdf', '')}_outline.json",
            mime="application/json"
        )
