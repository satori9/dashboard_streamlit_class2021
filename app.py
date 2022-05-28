import streamlit as st
from multiapp import MultiApp
import class2021
import all2021

PAGES = {
    "Result": class2021,
    "Analysis": all2021
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

app = MultiApp()
app.add_app("Result", class2021.app)
app.add_app("Analysis", all2021.app)
app.run()
