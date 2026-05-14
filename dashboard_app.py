import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import plotly.graph_objects as go

engine = create_engine('postgresql://postgres:0909@localhost:5432/training_shoes')

st.set_page_config(page_title="Top 10 Most Used Shoes in NBA 2024-2025 season", layout="wide")
st.markdown('<style>div.block-container {padding-top:3rem;}</style>', unsafe_allow_html=True)

# --- the heading image and the title ---
col1, col2 = st.columns([.1, .9])
with col1:
    st.image('shoe.png', width=200);

html_title = """
    <h1 style='text-align: center; color: #333;font_weight: bold;padding: 10px; border_radius: 5px; background-color: #f0f0f0;'>Top 10 Most Used Shoes in NBA 2024-2025 season</h1>
    """

with col2:
    st.markdown(html_title, unsafe_allow_html=True)

query = """
SELECT model, 
SUM(mins) AS mins 
FROM shoe GROUP BY model ORDER BY mins DESC 
LIMIT 10;
"""

sql_chart = pd.read_sql(query, engine)

# --- the bar chart ---
col3, col4 = st.columns([1, 1])

with col3:
    mins_chart = px.bar(sql_chart, x='model',  y='mins',text='model' )
    mins_chart.update_traces(textposition='outside')
    mins_chart.update_xaxes(tickmode='linear', tickangle=45)
    mins_chart.update_layout(title=dict(text='Top 10 Shoes by Total Minutes Played',x=0.5,xanchor='center'),
    xaxis_title='Shoe Model',yaxis_title='Total Minutes Played',height=600,showlegend=False,margin=dict(l=50, r=50, t=50, b=50)
)
st.plotly_chart(mins_chart, use_container_width=True)