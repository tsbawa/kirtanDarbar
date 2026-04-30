import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# --- HELPER: LOAD EXTERNAL CSS ---
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file '{file_name}' not found!")

# --- INITIALIZATION ---
st.set_page_config(page_title="Kirtan Darbar", page_icon="☬")
local_css("style.css") # Injects your styles right at the start

# Firebase Setup
if not firebase_admin._apps:
    cred = credentials.Certificate('firebase_config.json')
    firebase_admin.initialize_app(cred)
db = firestore.client()

# --- APP LAYOUT ---
st.markdown('<div class="hero"><h1 class="crimson">Kirtan Darbar</h1></div>', unsafe_allow_html=True)

# Example of a Search Bar using Streamlit's native widget
city_search = st.text_input("Enter City", placeholder="e.g. Amritsar")

# Displaying data inside your custom CSS classes
if city_search:
    st.markdown(f'''
        <div class="darbar-card">
            <h3 class="crimson">Evening Samagam</h3>
            <p class="gurmukhi">ਸਤਿਨਾਮੁ ਵਾਹਿਗੁਰੂ</p>
            <p>Location: {city_search}</p>
        </div>
    ''', unsafe_allow_html=True)
