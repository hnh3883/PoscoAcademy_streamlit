import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import graphviz
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import clear_output 
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
import io
import matplotlib.font_manager as fm
# 폰트 설치
font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"  # 사용할 폰트 파일 경로
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc("font", family=font_name)

# 배너 이미지
st.title("공정 운전조건 조절")


# 각 파라미터 슬라이더 조절
col1, col2, col3, col4, col5, col6  = st.columns(6)

Temp_OXid = col1.slider('Temp_OXid', 862, 1311, 1000)
ppm = col2.slider('ppm', 21, 49, 25)
Pressure = col3.slider('Pressure', 3, 10, 0)
Oxid_time = col4.slider('Oxid_time', 8, 291, 150)
N2_HMDS = col5.slider('N2_HMDS', 9, 23, 18)
pressure_HMDS = col6.slider('pressure_HMDS', 14, 15, 13)
# temp_HMDS = col7.slider('temp_HMDS', 19, 20, 19)


############################# 
# 경로 데이터
path1_data = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2)
]

path2_data = [
    (0, 1),
    (1, 0),
    (2, 0),
    (3, 1)
]

path3_data = [
    (0, 2),
    (1, 2),
    (2, 2),
    (3, 0)
]

# 그래프 생성
fig, ax = plt.subplots(figsize=(6, 4))

# 경로 그리기
x1, y1 = zip(*path1_data)
ax.plot(x1, y1, color='blue', linewidth=2)

x2, y2 = zip(*path2_data)
ax.plot(x2, y2, color='blue', linewidth=2)

x3, y3 = zip(*path3_data)
ax.plot(x3, y3, color='blue', linewidth=2)

# 공 그리기
positions = path1_data + path2_data + path3_data
for pos in positions:
    ax.plot(pos[0], pos[1], 'o', color='black', markersize=30)

ax.text(0.2, 0.9, 'Oxid 공정', ha='center', va='center', transform=ax.transAxes, fontsize=12)
ax.text(0.4, 0.9, 'pht-sb 공정', ha='center', va='center', transform=ax.transAxes, fontsize=12)
ax.text(0.6, 0.9, 'pht-lg 공정', ha='center', va='center', transform=ax.transAxes, fontsize=12)
ax.text(0.8, 0.9, 'etch 공정', ha='center', va='center', transform=ax.transAxes, fontsize=12)


# 그래프 축 범위 설정
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 3)

# 축 숨기기
ax.axis('off')
# 그래프제목
plt.title("현재 투입 경로")
# 그래프 출력
plt.show()


#######################

data = {
            'Oxid': [random.random() for _ in range(3)],
            'photo': [random.random() for _ in range(3)],
            'etch': [random.random() for _ in range(3)],
            'ion_imp': [random.random() for _ in range(3)]
        }
df = pd.DataFrame(data)

output = st.empty()

# output.dataframe(df)

def update_values2():
    # 새로운 값을 생성하여 데이터프레임의 값 업데이트
    df['Oxid'] = [random.random() for _ in range(3)]
    df['photo'] = [random.random() for _ in range(3)]
    df['etch'] = [random.random() for _ in range(3)]
    df['ion_imp'] = [random.random() for _ in range(3)]

# 불량률 0.9 이상이면 빨간색으로 경고 
highlighted_df = df.style.applymap(lambda x: 'background-color: red' if x >= 0.9 else '', subset=['Oxid', 'photo', 'etch', 'ion_imp'])


# while True:

#     # 1초 대기
#     time.sleep(1)
#     update_values2()
#     # st.text(df)
#     output.dataframe(highlighted_df)
        
col1, col2 = st.columns(2)
with col1:
    # 그래프 출력 및 상하 중앙 정렬
    col1.empty()
    col1.pyplot(fig)

# 2번 그래프
with col2:
    # 데이터프레임 출력 및 상하 중앙 정렬
    col2.empty()
    col2.markdown('<div style="text-align: center;"><span style="font-size: 14px;">각 챔버별 불량률 예측</span></div>', unsafe_allow_html=True)
    col2.dataframe(highlighted_df)

# CSS 스타일 적용
css = '''
<style>
.css-1l02zjm.e5i1odf1 {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    min-height: 300px;
}
</style>
'''
st.markdown(css, unsafe_allow_html=True)
st.markdown("---")
###########

# st.markdown("<h2> 실시간 불량률 확인 </h2>", unsafe_allow_html=True)
# def main():
#     csv_path = "/home/piai/다운로드/불량일확률.csv" 
#     # csv_path = st.text_input("Enter CSV file path:")

#     if csv_path:
#         try:
#             # CSV 파일을 DataFrame으로 읽어오기
#             df = pd.read_csv(csv_path)
#             df = df.drop(df.columns[0], axis=1)

#             # 첫 번째 행 가져오기
#             # first_row = df.iloc[0]

#             # 그래프 그리기
#             chart = st.line_chart(df.iloc[0:1])

#         except FileNotFoundError:
#             st.error("File not found. Please enter a valid file path.")

#         i = 2  # Start from the second row
#         while i < len(df)+1:
#             # Update the chart with new data
#             chart.line_chart(df.iloc[0:i])
#             i += 1

#             # 1초 간격으로 데이터 추가
#             time.sleep(1)
# # main문 실행
# if __name__ == "__main__":
#     main()
