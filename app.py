import wikipediaapi as wik
import streamlit as stl
import spacy 

k = spacy.load("en_core_web_sm")

name = stl.text_input("Enter Name")

if(stl.button("Analyze")):
    if(name != ""):
        fetch = k(wik.Wikipedia('en').page(name).summary)
        view =spacy.displacy.render(fetch,style="ent")
        stl.write(view,unsafe_allow_html=True)