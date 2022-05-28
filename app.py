import streamlit as st
from multiapp import MultiApp
import class2021
import all2021



app = MultiApp()
app.add_app("Result", class2021.app)
app.add_app("Analysis", all2021.app)
app.run()
