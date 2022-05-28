import streamlit as st
from multiapp import MultiApp
import (
    class2021,
    all2021,
)

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Home", class2021.app)
apps.add_app("Analysis", all2021.app)

# The main app
apps.run()