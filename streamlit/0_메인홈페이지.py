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

st.set_page_config(layout="wide", page_title="메인홈페이지")

image_path = "/home/piai/다운로드/배너.png"
st.image(image_path, use_column_width=True)


def main():
    # CSS 스타일 정의
    css = '''
    <style>
    body {
        background-color: #f4f4f4;
    }
    h1 {
        color: #333;
        text-align: center;
    }
    .container {
        width: 50%;
        margin: 0 auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    .container p {
        margin-top: 10px;
    }
    </style>
    '''

    # 페이지 레이아웃
    st.markdown(css, unsafe_allow_html=True)
    st.markdown('<h1>세계 최고를 꿈꾸는 Posil 전자</h1>', unsafe_allow_html=True)
    st.markdown(
    '''
    <div style="display: flex; justify-content: space-between;">
        <div class="container">
            <img src="https://cdn-icons-png.flaticon.com/512/3500/3500835.png" alt="이미지" style="width: 200px;">
            <p>최고의 품질</p>
        </div>
        <div class="container">
            <img src="https://cdn-icons-png.flaticon.com/512/3439/3439283.png" alt="이미지" style="width: 200px;">
            <p>고객과의 신뢰</p>
        </div>
        <div class="container">
            <img src="https://media.istockphoto.com/id/1257957057/ko/%EB%B2%A1%ED%84%B0/%ED%83%9D%EB%B0%B0-%EC%95%84%EC%9D%B4%EC%BD%98.jpg?s=170667a&w=0&k=20&c=u-CkZI5jOXn2NOh2P9w0Xm8Lb8vVyETZrFgpIkDqxAQ=" alt="이미지" style="width: 200px;">
            <p>납기 준수</p>
    </div>
    ''',
    unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()

#########################

css = '''
<style>
body {
    background-color: #f4f4f4;
}
h1 {
    color: #333;
    text-align: center;
}
.container {
    width: 25%;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}
.container img {
    width: 150px;
    border-radius: 50%;
    margin-bottom: 10px;
}
.container h2 {
    margin: 0;
    font-size: 18px;
}
.container p {
    margin-top: 10px;
    font-size: 14px;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)
st.markdown('<h1>Posil 전자의 연구원</h1>', unsafe_allow_html=True)

researchers = [
    {
        'name': '한지훈',
        'image': 'https://cdn-icons-png.flaticon.com/512/1941/1941446.png',
        'description': '웹페이지 구현'
    },
    {
        'name': '최예진',
        'image': 'https://cdn-icons-png.flaticon.com/512/3532/3532704.png',
        'description': '공정 안정성 분석'
    },
    {
        'name': '김시은',
        'image': 'https://cdn-icons-png.flaticon.com/512/2922/2922644.png',
        'description': '최적 경로 도출'
    },
    {
        'name': '송은호',
        'image': 'https://cdn-icons-png.flaticon.com/512/1941/1941497.png',
        'description': '데이터 분석 계획 수립'
    },
    {
        'name': '강승훈',
        'image': 'https://cdn-icons-png.flaticon.com/128/1941/1941499.png',
        'description': '불량 예측 모델링'
    },
    {
        'name': '황수현',
        'image': 'https://cdn-icons-png.flaticon.com/512/4086/4086577.png',
        'description': '운전조건 최적화'
    }
]

col1, col2, col3 = st.columns(3)

for i in range(0, len(researchers), 3):
    with col1:
        researcher = researchers[i]
        st.markdown(
            f'''
            <div class="container" style="width: 300px;">
                <img src="{researcher['image']}" alt="{researcher['name']}"">
                <h2>{researcher['name']}</h2>
                <p>{researcher['description']}</p>
            </div>
            ''',
            unsafe_allow_html=True
        )
        
    with col2:
        researcher = researchers[i+1]
        st.markdown(
            f'''
            <div class="container" style="width: 300px;">
                <img src="{researcher['image']}" alt="{researcher['name']}"">
                <h2>{researcher['name']}</h2>
                <p>{researcher['description']}</p>
            </div>
            ''',
            unsafe_allow_html=True
        )
        
    with col3:
        researcher = researchers[i+2]
        st.markdown(
            f'''
            <div class="container" style="width: 300px;">
                <img src="{researcher['image']}" alt="{researcher['name']}"">
                <h2>{researcher['name']}</h2>
                <p>{researcher['description']}</p>
            </div>
            ''',
            unsafe_allow_html=True
        )


# for researcher in researchers:
#     st.markdown(
#         f'''
#         <div class="container">
#             <img src="{researcher['image']}" alt="{researcher['name']}"">
#             <h2>{researcher['name']}</h2>
#             <p>{researcher['description']}</p>
#         </div>
#         ''',
#         unsafe_allow_html=True
#     )