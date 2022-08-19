import streamlit as st
import pandas as pd
import random

def setup():
    if 'year_options' not in st.session_state:
        years = []
        for i in range(1980, 2500):
            years.append(i)
            print(i)
        st.session_state['year_options'] = years
    if 'keywords' not in st.session_state:
        keywords = []
        for i in range(10000):
            keywords.append(str(i) + ' keyword')
        st.session_state['keywords'] = keywords
    if 'years_events' not in st.session_state:
        years = []
        for i in range(0, 6000):
            years.append(random.choice(st.session_state['year_options']))
        st.session_state['years_events'] = years
    if 'found_events' not in st.session_state:
        st.session_state['found_events'] = 0

def search():
    st.write('# Results')

def update_year_start():
    if  st.session_state.year_end <= st.session_state.year_start:
        st.session_state.year_start = st.session_state.year_end - 1
        possible_years = list(range(st.session_state.year_start, st.session_state.year_end))
        count = 0
        for year in st.session_state['years_events']:
            if year in possible_years:
                count += 1
        st.session_state['found_events'] = count

def update_year_end():
    if  st.session_state.year_start >= st.session_state.year_end:
        st.session_state.year_end = st.session_state.year_start + 1
#
#
#
#

setup()

st.write("""
    # Future Bot
    by mw*""")

col1, buff, col2 = st.columns([2,1,2])

with col1:
    st.selectbox('Chose start year: ', 
                 st.session_state['year_options'], 
                 key='year_start',
                 on_change=update_year_end)

with col2:
    st.selectbox('Chose end year: ', 
                 st.session_state['year_options'],
                 key='year_end',
                 on_change=update_year_start)

input_kw_all = st.multiselect('Choose mandatory keywords "ALL": ', st.session_state.keywords)

input_kw_any = st.multiselect('Choose optional keywords "ANY": ', st.session_state.keywords)

st.write('ALL:', str(input_kw_all))
st.write('ANY:', str(input_kw_any))

if st.button('Search the database'):
    search()

st.write('Found events: ', st.session_state['found_events'])
