import streamlit as st
import glob
from pathlib import Path
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer

diary_files = sorted(glob.glob('*.txt'))
diary = {}
analyzer = SentimentIntensityAnalyzer()
for diary_file in diary_files:
    with open(diary_file, 'r', encoding='utf-8') as file:
        diary_date = Path(diary_file).stem
        text = file.read()
        score = analyzer.polarity_scores(text)
        diary[diary_date] = score


for dt, sc in diary.items():
    print(dt, sc)

dates = list(diary.keys())
pos = [item['pos'] for item in diary.values()]
neg = [item['neg'] for item in diary.values()]

print(dates)
print(pos)
print(neg)

st.header('Diary tone')

st.subheader('Positivity')
labels = dict(x='Date', y='Positivity')
figure = px.line(x=dates, y=pos, labels=labels)
st.plotly_chart(figure, use_container_width=True)

st.subheader('Negativity')
labels = dict(x='Date', y='Negativity')
figure = px.line(x=dates, y=neg, labels=labels)
st.plotly_chart(figure, use_container_width=True)
