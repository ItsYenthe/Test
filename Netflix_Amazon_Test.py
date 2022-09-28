#!/usr/bin/env python
# coding: utf-8

# In[14]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.title("Netflix en Amazon Database")

netflix_basis = pd.read_csv('NetflixOriginals.csv')
netflix_extra = pd.read_csv('netflix_original_movie_data.csv')
amazon_prime_basis = pd.read_csv('amazon prime movies.csv')

# Plotten van percentage films per taal met dropdownbox voor amazon, netflix en beide
fig = go.Figure()

dropdown_buttons = [
    {'label': 'Amazon', 'method':'update',
    'args':[{'visible':[True, False]}, {'title':'Amazon'}]},
    {'label': 'Netflix', 'method':'update',
    'args':[{'visible':[False, True]}, {'title':'Netflix'}]},
    {'label': 'Beide', 'method':'update',
    'args':[{'visible':[True, True]}, {'title':'Beide'}]}
]

fig.add_trace(go.Bar(x = new_amazon.index, y = new_amazon['Percentage'], name = 'Amazon Prime films/series'))
fig.add_trace(go.Bar(x = new_netflix.index, y = new_netflix['Percentage'], name = 'Netflix films/series'))
fig.update_layout({'updatemenus':[{'type': 'dropdown',
                                 'x':1.18, 'y':0.5,
                                 'showactive':True,
                                 'active': 0,
                                 'buttons':dropdown_buttons}]},
                  title_text = 'Aantal films/series die beschikbaar zijn via amazon of netflix, verdeeld per taal', yaxis_tickformat="2%",
                 )
fig.update_xaxes(title_text = 'Taal')
fig.update_yaxes(title_text = 'Percentage films')

st.plotly_chart(fig, use_container_width = True)

# Wij gaan kijken naar de 5 genres die het vaakt voorkomen
netflix['Genre'].value_counts()

# Selecteren naar de data waarbij het 1 van die 5 genres is
netflix_genre = netflix.loc[(netflix['Genre'] == 'Documentary') | (netflix['Genre'] == 'Drama')| (netflix['Genre'] == 'Comedy') | 
            (netflix['Genre'] == 'Thriller') | (netflix['Genre'] == 'Romantic comedy')]

# Plotten van de IMDB Scores per genre
my_scale = ['rgb(0, 171, 169)', 'rgb(0, 138, 0)', 'rgb(96, 169, 23)', 'rgb(164, 196, 0)', 'rgb(227, 200, 0)']
fig = px.box(data_frame = netflix_genre, x = 'Genre', y = 'IMDB Score', color = 'Genre', 
             color_discrete_sequence= my_scale, title = 'IMDB Scores per genre')

my_buttons = [{'label':'Boxplot', 'method':'update', 'args': [{'type': 'box'}]}, 
              {'label':'Violin', 'method':'update', 'args': [{'type': 'violin'}]}]

fig.update_layout({'updatemenus':[{'type': 'buttons', 'direction': 'down', 'x': 1.13, 'y': 0.5, 'showactive': True,
                                  'active': 0, 'buttons': my_buttons}]})

st.plotly_chart(fig, use_container_width = True)

# Visualisatie van runtime van de (Netflix)films tegen de IMDB scores !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
fig = go.Figure()

for runtime in ['0-50', '51-100', '101-150', '151-250']:
    df = netflix[netflix['Runtime_group'] == runtime]
    fig.add_trace(go.Box(x = df['Runtime_group'], y = df['IMDB Score'], name = runtime))
    
sliders = [{'steps':[
    {'label':'all', 'method': 'update', 'args': [{'visible': [True, True, True, True]}, {'title': 'Runtime'}]},
    {'label':'0-50 minuten', 'method': 'update', 'args': [{'visible': [True, False, False, False]}, {'title': 'Runtime van 0-50 minuten'}]},
    {'label':'51-100 minuten', 'method': 'update', 'args': [{'visible': [False, True, False, False]}, {'title': 'Runtime van 51-100 minuten'}]},
    {'label':'101-150 minuten', 'method': 'update', 'args': [{'visible': [False, False, True, False]}, {'title': 'Runtime van 101-150 minuten'}]},
    {'label':'151-250 minuten', 'method': 'update', 'args': [{'visible': [False, False, False, True]}, {'title': 'Runtime van 151-250 minuten'}]},
]}]

fig.update_xaxes(title_text = 'Runtime (minuten)')
fig.update_yaxes(title_text = 'IMDB Score')
fig.update_layout({'sliders': sliders})

st.plotly_chart(fig, use_container_width = True)

# Wij gaan kijken naar de 5 countries die het vaakt voorkomen
netflix['Country'].value_counts()

# Selecteren naar de data waarbij het 1 van die 5 genres is
netflix_country = netflix.loc[(netflix['Country'] == 'United states') | (netflix['Country'] == 'India')| (netflix['Country'] == 'United Kingdom') | 
            (netflix['Country'] == 'Spain') | (netflix['Country'] == 'France')]

dropdown_buttons3 = [
    {'label': 'All', 'method':'update',
    'args':[{'visible':[True, True, True, True]}, {'title':'Alle landen'}]},
    {'label': 'United States', 'method':'update',
    'args':[{'visible':[True, False, False, False, False]}, {'title':'United States'}]},
    {'label': 'India', 'method':'update',
    'args':[{'visible':[False, True, False, False, False]}, {'title':'India'}]},
    {'label': 'United Kindom', 'method':'update',
    'args':[{'visible':[False, False, True, False, False]}, {'title':'United Kingdom'}]},
    {'label': 'Spain', 'method':'update',
    'args':[{'visible':[False, False, False, True, False]}, {'title':'Spain'}]},
    {'label': 'France', 'method':'update',
    'args':[{'visible':[False, False, False, False, True]}, {'title':'France'}]}
]

# Plotten van percentage films per taal met dropdownbox voor amazon, netflix en beide
fig = go.Figure()

for country in ['United States', 'India', 'United Kingdom', 'Spain', 'France']:
    df = netflix[netflix['Country'] == country]
    fig.add_trace(go.Box(x = df['Country'], y = df['IMDB Score'], name = country))

fig.update_layout({'updatemenus':[{'type': 'dropdown',
                                 'x':1.21, 'y':0.5,
                                 'showactive':True,
                                 'active': 0,
                                 'buttons':dropdown_buttons3}]},
                  title_text = 'IMDB Score land'
                 )
fig.update_xaxes(title_text = 'Country')
fig.update_yaxes(title_text = 'IMDB Score')

st.plotly_chart(fig, use_container_width = True)


# In[2]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




