import streamlit as st

about_page = st.Page(
    page="Views/aboutme.py",
    title="About Me",
    # icon=":material/account_circles:",
    default=True,
)
project_1_page = st.Page(
    page="Views/chatboat.py",
    title="Chatbot",
    # icon=":material/smart_toys:",
)

# --Navigation Bar--

pg = st.navigation(
    {
        "Info":[about_page],
        "Projects":[project_1_page]
    }
)

# --Navigation Run--

pg.run()

# st.logo("")
st.sidebar.text("Made by Me")