import streamlit as st

about_page = st.Page(
    page="Views/aboutme.py",
    title="About Me",
    # icon=":material/account_circles:",
    default=True,
)

pg = st.navigation(
    {
        "Info":[about_page]
    }
)

# --Navigation Run--

pg.run()

# st.logo("")
st.sidebar.text("Made by Me")