import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('プログレスバー')
st.write('プログレスバーの表示')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Loading {i+1} % done.')
    bar.progress(i+1)
    time.sleep(0.05)
time.sleep(0.1)
latest_iteration.empty()
bar.empty()

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

st.sidebar.write('Widgets')
text = st.sidebar.text_input('Input your hobby')
condition = st.sidebar.slider('How are you?', 0, 100, 50)

msg_hobby = 'Your Hobby is {}. Cool!'.format(text)
msg_condition = 'Your Condition is {:>3d}'.format(condition)

left_column, right_column = st.beta_columns(2)
left_column.write(msg_hobby)

button = right_column.button('右カラム表示')
if button:
    right_column.write('右カラムに表示されている')
    right_column.write(msg_condition)

expander1 = st.beta_expander('問い合わせ１')
expander1.write('問い合わせ１の内容')
expander2 = st.beta_expander('問い合わせ２')
expander2.write('問い合わせ２の内容')
expander3 = st.beta_expander('問い合わせ３')
expander3.write('問い合わせ３の内容')
