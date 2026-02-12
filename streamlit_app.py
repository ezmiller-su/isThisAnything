import streamlit as st
import json
import random

st.set_page_config(page_title="Is This Something?", page_icon=None, layout="wide", menu_items=None)

with open('seinfeld_bits.json', 'r') as file:
    data = json.load(file)

n = sum(1 for line in data)-1

x = random.randrange(0,n)

st.title(data[x]["title"])

st.text(data[x]["body"])

#test