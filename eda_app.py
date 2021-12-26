import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run_eda_app():
    
    st.sidebar.header('<목록>')
    st.sidebar.subheader('1)시도별 발생건수 그래프')
    st.sidebar.subheader('2)시도별 사망자수 그래프')  

    st.sidebar.subheader('3)시도별 부상자수 그래프')
    st.sidebar.subheader('4)시도별 중상 그래프')
    
    st.sidebar.subheader('5)시도별 경상 그래프')
    st.sidebar.subheader('6)시도별 부상신고 그래프')

    

    df=pd.read_csv('data/도로교통.csv',encoding='CP949')
    df1=df.loc[:,'발생건수':'부상신고']
    fig = px.bar(        
        df,
        x = "시도",
        y = "발생건수",
        title = "시도별 발생건수"
        )
    st.plotly_chart(fig)    
    fig1 = px.bar(        
        df,
        x = "시도",
        y = "사망자수",
        title = "시도별 사망자수"
        )
    st.plotly_chart(fig1)    
    fig2 = px.bar(        
        df,
        x = "시도",
        y = "부상자수",
        title = "시도별 부상자수"
        )
    st.plotly_chart(fig2)    
    fig3 = px.bar(        
        df,
        x = "시도",
        y = "중상",
        title = "시도별 중상"
        )
    st.plotly_chart(fig3)    
    fig4 = px.bar(        
        df,
        x = "시도",
        y = "경상",
        title = "시도별 경상"
        )
    st.plotly_chart(fig4)    
    fig5 = px.bar(        
        df,
        x = "시도",
        y = "부상신고",
        title = "시도별 부상신고"
        )   
    st.plotly_chart(fig5)    

   
    
    
    
   

       


    # 상관계수 분석을 위한, 상관계수 보여주는 화면 개발
    

    #문자열 데이터가 아닌 컬럼들만 가져오는 코드
   


    #유저가 컬럼을 선택하면
    #해당 컬럼의min과 max에 해당하는 사람이 누구인지
    #그 사람의 데이터를 화면에 보여주는 기능 개
    # print(df.dtypes != object)

    # print(df.columns[df.dtypes != object])
    # number_columns=df.columns[df.dtypes != object]

    # selected_minmax_column=st.selectbox('컬럼선택',number_columns)

    # #선택한 컬럼의 최소값에 해당되는 사람의 데이터 출력
    # min_data=df[selected_minmax_column]==df[selected_minmax_column].min
    # st.dataframe(min_data)
    # #선택한 컬럼의 최대값에 해당되는 사람의 데이터 출력
    
    # max_data=df[selected_minmax_column]==df[selected_minmax_column].max
    # st.dataframe(max_data)
    # #고객의 이름을 검색할 수 있는 기능 개발
    # st.subheader('발생건수')
    # #1. 유저한테 검색어 입력을 받습니다.
    # word=st.text_input('검색어를 입력하세요')
    # print(word)
    # #2.검색어를 데이터프레임의 Customer Name컬럼에서 검색해서 가져온다
    
    # df_search=df.loc[df['시군구'].str.lower().str.contains(word),]
    # #3.화면에 결과를 보여준다
    # st.dataframe(df_search)