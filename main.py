import streamlit as st
from multipage import MultiApp
from halaman import home, data, inputData # import your app modules here
from streamlit_option_menu import option_menu
from Kriptografi import Kriptografi


st.set_page_config(page_title='OxidiLily',layout='wide')
hidden_menu = """
<style>
#MainMenu{
    visibility : hidden;
    }
footer {
    visibility : hidden;
    }

div.stAlert{
  text-align: center;
}
</style>
"""
app = MultiApp()
st.markdown(hidden_menu,unsafe_allow_html=True)


selected = option_menu(
        menu_title =None,
        options = ['Home','Input Data', 'Dataset', 'Kriptografi'],
        icons = ["house", "book", "person-fill","unlock"],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal",
)
    
if selected == 'Home':
    app.add_app("Home", home.app)
   
if selected == 'Input Data':
    app.add_app("Input Data", inputData.app)

if selected == 'Dataset':
    app.add_app("Data", data.app)  

if selected == 'Kriptografi':
    app.add_app("Kriptografi", Kriptografi.app)    

app.run()
