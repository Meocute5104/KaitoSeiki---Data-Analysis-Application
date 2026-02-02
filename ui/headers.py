from pathlib import Path
import streamlit as st

def render_header():
    logo_path = Path("assets/logo/logo01.svg")

    if logo_path.exists():
        st.markdown(
            '<div style="text-align:center; margin-bottom:20px;">',
            unsafe_allow_html=True
        )
        st.image(str(logo_path), width=220)
        st.markdown('</div>', unsafe_allow_html=True)
