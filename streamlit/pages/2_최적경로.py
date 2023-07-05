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

# 경로 데이터

if st.button("Update Paths"):

    st.markdown('<div style="text-align: center;"><span style="font-size: 14px;">경로 조합 별 불량확률 정렬</span></div>', unsafe_allow_html=True)

    path1_data = []
    path2_data = []
    path3_data = []
    path4_data = []
    path5_data = []
    path6_data = []
    path7_data = []
    path8_data = []
    path9_data = []

    for i in range(4):
        options = [0, 1, 2]
        rand_num1 = random.choice(options)
        options.remove(rand_num1)
        rand_num2 = random.choice(options)
        options.remove(rand_num2)
        rand_num3 = options[0]

        path1_data.append((i, rand_num1))
        path2_data.append((i, rand_num2))
        path3_data.append((i, rand_num3))

    result1 = ""
    result2 = ""
    result3 = ""

    for row in path1_data:
        result1 += str(row[1])
    for row in path2_data:
        result2 += str(row[1])
    for row in path3_data:
        result3 += str(row[1])

    for i in range(4):
        options = [0, 1, 2]
        rand_num4 = random.choice(options)
        options.remove(rand_num4)
        rand_num5 = random.choice(options)
        options.remove(rand_num5)
        rand_num6 = options[0]

        path4_data.append((i, rand_num4))
        path5_data.append((i, rand_num5))
        path6_data.append((i, rand_num6))

    result4 = ""
    result5 = ""
    result6 = ""

    for row in path4_data:
        result4 += str(row[1])
    for row in path5_data:
        result5 += str(row[1])
    for row in path6_data:
        result6 += str(row[1])

    for i in range(4):
        options = [0, 1, 2]
        rand_num7 = random.choice(options)
        options.remove(rand_num7)
        rand_num8 = random.choice(options)
        options.remove(rand_num8)
        rand_num9 = options[0]

        path7_data.append((i, rand_num7))
        path8_data.append((i, rand_num8))
        path9_data.append((i, rand_num9))

    result7 = ""
    result8 = ""
    result9 = ""

    for row in path7_data:
        result7 += str(row[1])
    for row in path8_data:
        result8 += str(row[1])
    for row in path9_data:
        result9 += str(row[1])

    random_value1 = random.uniform(0, 0.034)
    random_value2 = random.uniform(0.034, 0.068)
    random_value3 = random.uniform(0.068, 0.123)

    data = {
        '우선순위': [1,2,3],
        'Group1': [result1,result4,result7],
        'Group2': [result2,result5,result8],
        'Group3': [result3,result6,result9],
        '불량확률': [random_value1,random_value2,random_value3]
    }

    df = pd.DataFrame(data)
    st.table(df)

    # 그래프 생성
    fig, ax = plt.subplots()

    # 경로 그리기
    for point in path1_data:
        ax.plot(point[0], point[1], 'o', color='black', markersize=30)

    x1, y1 = zip(*path1_data)
    ax.plot(x1, y1, color='blue', linewidth=2)

    for point in path2_data:
        ax.plot(point[0], point[1], 'o', color='black', markersize=30)

    x2, y2 = zip(*path2_data)
    ax.plot(x2, y2, color='blue', linewidth=2)

    for point in path3_data:
        ax.plot(point[0], point[1], 'o', color='black', markersize=30)

    ax.text(0.2, 0.9, 'Oxid 공정', ha='center', va='center', transform=ax.transAxes, fontsize=12)
    ax.text(0.4, 0.9, 'pht-sb 공정', ha='center', va='center', transform=ax.transAxes, fontsize=12)
    ax.text(0.6, 0.9, 'pht-lg 공정', ha='center', va='center', transform=ax.transAxes, fontsize=12)
    ax.text(0.8, 0.9, 'etch 공정', ha='center', va='center', transform=ax.transAxes, fontsize=12)

    x3, y3 = zip(*path3_data)
    ax.plot(x3, y3, color='blue', linewidth=2)

    # 그래프 축 범위 설정
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 3)

    # 축 숨기기
    ax.axis('off')

    # Streamlit 앱
    st.markdown('<div><span style="font-size: 20px;">최적 Path 탐색</span></div>', unsafe_allow_html=True)
    st.markdown("다음 투입될 웨이퍼의 경로는 아래와 같습니다.", unsafe_allow_html=True)


    # 그래프 크기 조절
    # fig.set_size_inches(8, 6)  # 가로 8인치, 세로 6인치

    # # 그래프 출력
    # st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        # 그래프 출력 및 상하 중앙 정렬
        col1.empty()
        col1.pyplot(fig)
    # 2번 그래프
    with col2:
        # 데이터프레임 출력 및 상하 중앙 정렬
        col2.empty()
        # col2.markdown('<div style="text-align: center;"><span style="font-size: 14px;">각 챔버별 불량률 예측</span></div>', unsafe_allow_html=True)
        # col2.dataframe(highlighted_df)
    # with col3:
    #     # 데이터프레임 출력 및 상하 중앙 정렬
    #     col3.empty()
