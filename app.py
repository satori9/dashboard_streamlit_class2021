import streamlit as st
from multiapp import MultiApp
from apps import (class2021,  all2021)

apps = MultiApp()

# Add all your application here
apps.add_app("Result", class2021.app)
apps.add_app("Analysis", all2021.app)

# The main app
apps.run()
