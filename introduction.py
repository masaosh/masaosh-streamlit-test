import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit入門')

st.write('DataFrame')

#df = pd.DataFrame({
#    '1列目': [1,2,3,4],
#    '2列目': [10, 20, 30, 40]
#})

df= pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)

#st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
st.dataframe(df.style.highlight_max(axis=0))

#st.write('Static table')
#st.table(df.style.highlight_max(axis=0))

st.write('折れ線グラフ')
st.line_chart(df)

st.write('エリアチャート')
st.area_chart(df)

st.write('棒グラフ')
st.bar_chart(df)

df2= pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
#st.write(df2)

st.write('マップ')
st.map(df2)

st.write('画像表示')
img = Image.open('../sample.jpeg')
st.image(img, caption='sample', use_column_width=True)

#Markdown
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as numpy
import pandas as pd
```
"""