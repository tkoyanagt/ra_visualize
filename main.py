import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit をいじってみた！')

st.write('DataFrame')

df = pd.DataFrame(
	np.random.rand(20,3),
	columns = ['a', 'b', 'c']
)
df

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df2 = pd.DataFrame(
	np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
	columns=['lat', 'lon']
	)
df2

st.map(df2)


img = Image.open('matchi.png')
st.image(img, caption='待っている人', use_column_width=True)








