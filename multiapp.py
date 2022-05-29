import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    #def run(self):
     #   app = st.sidebar.radio(
     #       'Go To',
     #       self.apps,
     #       format_func=lambda app: app['title'])

    #    app['function']()
        
    def run(self):
        app_state = st.experimental_get_query_params()
        app_state = {
            k: v[0] if isinstance(v, list) else v for k, v in app_state.items()
        }  # fetch the first item in each query string as we don't have multiple values for each query string key in this example

        # st.write('before', app_state)

        titles = [a["title"] for a in self.apps]
        functions = [a["function"] for a in self.apps]
        default_radio = titles.index(app_state["page"]) if "page" in app_state else 0

        st.sidebar.title("2021年度色彩トレーニング")

        title = st.sidebar.radio("Go To", titles, index=default_radio, key="radio")

        app_state["page"] = st.session_state.radio
        # st.write('after', app_state)

        st.experimental_set_query_params(**app_state)
        # st.experimental_set_query_params(**st.session_state.to_dict())
        functions[titles.index(title)]()
