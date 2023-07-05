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

st.set_page_config(
    page_title="실시간모니터링"
)

st.title("실시간 모니터링")
#########################################
selected_columns = ['type','Temp_OXid', 'Vapor', 'ppm','Pressure', 'Oxid_time',
                   'N2_HMDS', 'pressure_HMDS', 'temp_HMDS', 'temp_HMDS_bake', 'time_HMDS_bake', 'spin1', 'spin2', 'spin3','photoresist_bake','temp_softbake', 'time_softbake',
                    'UV_type', 'Wavelength','Energy_Exposure',
                    'Source_Power','Temp_Etching',
                    'input_Energy','Temp_implantation','Furance_Temp', 'RTA_Temp',
                     'Target'
                   ]

#########################################
# 슬라이더 기능 추가
with st.sidebar:
    st.title("컨트롤 인자 파라미터 조절")

    Temp_OXid = st.slider('Temp_OXid', 862, 1311, 1000, format="%d 3px")
    ppm = st.slider('ppm', 21, 49, 25)
    Pressure = st.slider('Pressure', 0, 1, 0)
    Oxid_time = st.slider('Oxid_time', 8, 291, 150)
    N2_HMDS = st.slider('N2_HMDS', 9, 23, 18)
    pressure_HMDS = st.slider('pressure_HMDS', 14, 15, 13)
    temp_HMDS = st.slider('temp_HMDS', 19, 20, 19)
# temp_HMDS_bake = st.slider('temp_HMDS_bake', 191, 209, 205)
# time_HMDS_bake = st.slider('time_HMDS_bake', 90, 91, 90)
# spin1 = st.slider('spin1', 492, 509, 500)
# spin2 = st.slider('spin2', 3864, 4208, 3956)
# spin3 = st.slider('spin3', 4814, 5194, 5046)
# photoresist_bake = st.slider('photoresist_bake', 4, 5, 5)
# temp_softbake = st.slider('temp_softbake', 86, 96, 91)
# time_softbake = st.slider('time_softbake', 29, 30, 30)
# Energy_Exposure = st.slider('Energy_Exposure', 111, 112, 111)
# Temp_Etching = st.slider('Temp_Etching', 68, 73, 70)
# Source_Power = st.slider('Source_Power', 49, 53, 51)
# input_Energy = st.slider('input_Energy', 29604, 33675, 31657)
# Temp_implantation = st.slider('Temp_implantation', 97, 107, 100)
# Furance_Temp = st.slider('Furance_Temp', 854, 944, 926)
# RTA_Temp = st.slider('RTA_Temp', 148, 162, 151)

#########################################
# 파라미터 소개

col1, col2, col3, col4, col5, col6, col7 = st.beta_columns(7)
#, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20, col21, col22

# 첫 번째 metric
with col1:
    st.metric(label="Temp_OXid", value=Temp_OXid, delta="1.2 °C")

# 두 번째 metric
with col2:
    st.metric(label="ppm", value=ppm)
with col3:
    st.metric(label="Pressure", value=Pressure)
with col4:
    st.metric(label="Oxid_time", value=Oxid_time)
with col5:
    st.metric(label="N2_HMDS", value=N2_HMDS)
with col6:
    st.metric(label="pressure_HMDS", value=pressure_HMDS)
with col7:
    st.metric(label="temp_HMDS", value=temp_HMDS)
# with col8:
#     st.metric(label="temp_HMDS_bake", value=temp_HMDS_bake)
# with col9:
#     st.metric(label="time_HMDS_bake", value=time_HMDS_bake)
# with col10:
#     st.metric(label="spin1", value=spin1)
# with col11:
#     st.metric(label="spin2", value=spin2)
# with col12:
#     st.metric(label="spin3", value=spin3)
# with col13:
#     st.metric(label="photoresist_bake", value=photoresist_bake)
# with col14:
#     st.metric(label="temp_softbake", value=temp_softbake)
# with col15:
#     st.metric(label="time_softbake", value=time_softbake)
# with col16:
#     st.metric(label="Energy_Exposure", value=Energy_Exposure)
# with col17:
#     st.metric(label="Temp_Etching", value=Temp_Etching)
# with col18:
#     st.metric(label="Source_Power", value=Source_Power)
# with col19:
#     st.metric(label="input_Energy", value=input_Energy)
# with col20:
#     st.metric(label="Temp_implantation", value=Temp_implantation)
# with col21:
#     st.metric(label="Furance_Temp", value=Furance_Temp)
# with col22:
#     st.metric(label="RTA_Temp", value=RTA_Temp)


#########################################
# 경로 만들기

#반도체 경로 데이터
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
fig, ax = plt.subplots()

# 애니메이션 함수
def update_animation(i):
    ax.clear()

    # 1번 path 동그라미 그리기
    for point in path1_data[:i+1]:
        ax.plot(point[0], point[1], 'o', color='black', markersize=30)
    # 2번 path 동그라미 그리기
    for point in path2_data[:i+1]:
        ax.plot(point[0], point[1], 'o', color='black', markersize=30)
    # 3번 path 동그라미 그리기
    for point in path3_data[:i+1]:
        ax.plot(point[0], point[1], 'o', color='black', markersize=30)

    # 경로 그리기
    x1, y1 = zip(*path1_data[:i+1])
    ax.plot(x1, y1, color='blue', linewidth=2)

    x2, y2 = zip(*path2_data[:i+1])
    ax.plot(x2, y2, color='blue', linewidth=2)

    x3, y3 = zip(*path3_data[:i+1])
    ax.plot(x3, y3, color='blue', linewidth=2)

    # 그래프 축 범위 설정
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 3)

    # 축 숨기기
    ax.axis('off')

# Streamlit 앱
st.title("Path")

# 애니메이션 플롯 생성
animation_plot = st.pyplot(fig)

# 애니메이션 실행
for i in range(len(path1_data)):
    update_animation(i)
    animation_plot.pyplot(fig)
    st.empty()






#########################################
# 버튼 생성

toggle_state = False

toggle_button = st.checkbox("불량확률 확인")

if toggle_button:
    toggle_state = not toggle_state  # 토글 상태 업데이트
    if toggle_state:
        st.write("토글스위치: 켜짐")
        # 3행 4열의 빈 데이터프레임 생성
        data = {
            'Oxid': [random.random() for _ in range(3)],
            'photo': [random.random() for _ in range(3)],
            'etch': [random.random() for _ in range(3)],
            'ion_impl': [random.random() for _ in range(3)]
        }
        df = pd.DataFrame(data)

        output = st.empty()

        output.dataframe(df)

        def update_values2():
            # 새로운 값을 생성하여 데이터프레임의 값 업데이트
            df['Oxid'] = [random.random() for _ in range(3)]
            df['photo'] = [random.random() for _ in range(3)]
            df['etch'] = [random.random() for _ in range(3)]
            df['ion_impl'] = [random.random() for _ in range(3)]

        # 불량률 0.9 이상이면 빨간색으로 경고 
        highlighted_df = df.style.applymap(lambda x: 'background-color: red' if x >= 0.9 else '', subset=['Oxid', 'photo', 'etch', 'ion_impl'])


        while True:

            # 1초 대기
            time.sleep(1)
            update_values2()
            # st.text(df)
            output.dataframe(highlighted_df)

#########################################
# 작업완료 창
st.divider()
lot_number = random.randint(0, 10)
st.subheader('LOT {}번 작업 완료'.format(lot_number))
st.divider()


#########################################
# 경로 별 불량률 오름차순 정렬

# data = {
#     '우선순위' : [1, 2, 3],
#     'Group1': [1223, 1223, 1213],
#     'Group2': [2131, 2132, 2121],
#     'Group3': [3312, 3311, 3332],
#     '불량률': [0.034, 0.036, 0.037]
# }

# df = pd.DataFrame(data)

# # 테이블 출력
# st.table(df)

#########################################3
# 경로 데이터

if st.button("Update Paths"):
    path1_data = []
    path2_data = []
    path3_data = []

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


    result1 = ''
    result2 = ''
    result3 = ''

    for row in path1_data:
        result1 += str(row[1])
    for row in path2_data:
        result2 += str(row[1])
    for row in path3_data:
        result3 += str(row[1])


    data = {
        '우선순위': [1],
        'Group1': [result1],
        'Group2': [result2],
        'Group3': [result3],
        '불량률': [0.034]
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

    x3, y3 = zip(*path3_data)
    ax.plot(x3, y3, color='blue', linewidth=2)

    # 그래프 축 범위 설정
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 3)

    # 축 숨기기
    ax.axis('off')

    # Streamlit 앱
    st.title("Path")

    # 그래프 표시
    st.pyplot(fig)

    #########################################
# 실시간 불량률 그래프

def main():
    csv_path = st.text_input("Enter CSV file path:")

    if csv_path:
        try:
            # CSV 파일을 DataFrame으로 읽어오기
            df = pd.read_csv(csv_path)
            df = df.drop(df.columns[0], axis=1)

            # 첫 번째 행 가져오기
            # first_row = df.iloc[0]

            # 그래프 그리기
            chart = st.line_chart(df.iloc[0:1])

        except FileNotFoundError:
            st.error("File not found. Please enter a valid file path.")

        i = 2  # Start from the second row
        while i < len(df)+1:
            # Update the chart with new data
            chart.line_chart(df.iloc[0:i])
            i += 1

            # 1초 간격으로 데이터 추가
            time.sleep(1)

# main문 실행
if __name__ == "__main__":
    main()
