import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('インタラクティブなウィジェット')

st.write('チェックボックス')
if st.checkbox('Show Image'):
    img = Image.open('../sample.jpeg')
    st.image(img, caption='sample', use_column_width=True)

st.write('セレクトボックス')
option = st.selectbox(
    'Please tell me your favorite number!',
    list(range(1, 11))
)
'Your favorite number is ', option, '!' 

st.write('テキスト入力')
text = st.text_input('Input your hobby')
'Your Hobby is ', text, '. Cool!'

st.write('スライダー')
condition = st.slider('How are you?', 0, 100, 50)
'Your Condition is ', condition
