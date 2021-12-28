import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import seaborn as sb
import plotly.express as px
import altair as alt





def run_ml_app() :
    st.sidebar.header('<목록>')
    st.sidebar.subheader('1)상관계수')
    st.sidebar.subheader('2)특정지역 자료분석')  
   
  
    df=pd.read_csv('data/도로교통.csv',encoding='CP949')
    st.subheader('상관계수')
    sb.set(font="Malgun Gothic", rc={"axes.unicode_minus":False}, style='darkgrid')
    sb.scatterplot(data=df)
    
    df_corr=df.iloc[:,3:]
   

    selected_corr=st.multiselect('상관계수 컬럼 선택',df_corr.columns)

    if len(selected_corr)>0:
        st.table(df_corr[selected_corr].corr())

        #상관계수를 수치로도 구하고 차트로도 표시하라
        fig1=sb.pairplot(data=df_corr[selected_corr])
        
        st.pyplot(fig1) 

    #유저가 컬럼을 선택하지 않은 경우
    else:
        st.write('선택한 컬럼이 없습니다.')

    result=st.checkbox('상관계수 해석 참고')
    if result:
        st.write('상관계수가 -1.0과 -0.7 사이이면, 강한 음적 선형관계')
        st.write('상관계수가 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계')
        st.write('상관계수가 -0.3과 -0.1 사이이면, 약한 음적 선형관계')
        st.write('상관계수가 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계')
        st.write('상관계수가 +0.1과 +0.3 사이이면, 약한 양적 선형관계')
        st.write('상관계수가 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계')
        st.write('상관계수가 +0.7과 +1.0 사이이면, 강한 양적 선형관계')
  
    #고객의 이름을 검색할 수 있는 기능 개발
    st.subheader('특정지역 자료분석')
    #1. 유저한테 검색어 입력을 받습니다.
    word=st.text_input('시군구를 검색창에 입력하세요')
    print(word)
    #2.검색어를 데이터프레임의 Customer Name컬럼에서 검색해서 가져온다
    df_search=df.loc[df['시군구'].str.contains(word)]
    # df_search=df.loc[df['시군구'].str.lower().str.contains(word),]
    #3.화면에 결과를 보여준다
    st.table(df_search)
    df_search 
    
  
    
 
  