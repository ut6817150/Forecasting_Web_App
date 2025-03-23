import streamlit as st
import pandas as pd
import os
import json


st.set_page_config(
    page_title="Client Dataset"
)

# Setup data 
client_data = pd.read_csv('06_Web_Application/client_219_153_baseline.csv')

# Chaning dates to datetime
client_data['StatusCreatedDate'] = pd.to_datetime(client_data['StatusCreatedDate'], infer_datetime_format=True)

client_data = client_data.head(30)

# Make Page
st.write("""
# Sales Prediction App
Deployment of client dataset machine learning model using **XGBoost**.
This app predicts the **Weekly Sales over a Booking Period**

Use this dashboard to understand the data and to make preditions.
""")

st.write('---')
st.write('**Desription of Prediction Dataset**')
st.write('**Weeks to Event** - number of weeks to event start date')
st.write('**EventType** - represents the event type of the event name')
st.write('**StatusCreatedDate** - marks the data bookings were placed by the atendee')
st.write('**Num_of_ticket** - represents the number of tickets booked per event for each booking day')
st.write('---')
st.subheader('Below outlines each "Others, Group" Event Names grouping in EventType')
st.write('**Others, Group 1** - EventIds begining with 14 - Reading & Writing and Teaching')
st.write('**Others, Group 2** - EventIds begining with 15 - Gymnastics, School, Disability')
st.write('**Others, Group 3** - EventIds begining with 16 - Professional Development, Language, Teaching, Conference')
st.write('**Others, Group 4** - EventIds begining with 17 - Teaching, webinars, Professional Development')
st.write('**Others, Group 5** - EventIds begining with 18 - Conference')
st.write('**Others, Group 6** - EventIds begining with 19 - Management, Webinar, School')
st.write('**Others, Group 7** - EventIds begining with 20 - Exam, Training, Introduction')
st.write('**Others, Group 8** - EventIds begining with 21 - Empowerment, Global Skills, Professional Development')
st.write('**Others, Group 9** - EventIds begining with 22 - Global Skills, Professional Development, Language')
st.write('**Others, Group 10** - EventIds begining with 23- 27 - Conference, Language, Geography, History')
st.write('---')
# Dsiplaying preview of Datframe
st.write('**Sample of Prediction Dataset**')
st.dataframe(client_data)