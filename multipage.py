import streamlit as st

class MultiApp:
    
    def __init__(self):
        self.apps = []

    #Func Buat Nambah Halaman
    def add_app(self, title, func):
       
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # app = st.sidebar.selectbox(
        app = st.radio('',
            self.apps,
            format_func=lambda app: app['title'],
            disabled=True,)

        app['function']()