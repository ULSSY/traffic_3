import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def run_now_app():
    now=st.sidebar.selectbox("왼쪽 사이드바 Select Box", ("인천", "경기", "강원",'서울','세종','충북','충남','광주','대전','전북','전남','대구','부산','울산','경북','경남'))

    df=pd.read_csv('data/도로교통.csv',encoding='CP949')
    
    
    if now=='인천':
        df=df.loc[143:150,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
         
    elif now=='경기':
        df=df.loc[18:44,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
          
    elif now=='강원'   :
        df=df.loc[45:54,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
          
    elif now=='서울'  :
        df=df.loc[2:11,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
         
    elif now=='세종' :
       
        df={'발생건수':4,'사망자수':0,'부상자수':9,'중상':1,'경상':8,'부상신고':0}
        st.write(df)
        # fig = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "발생건수",
        #     title = "시군구별 발생건수"
        #     )
        # st.plotly_chart(fig)
        # fig1 = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "사망자수",
        #     title = "시군구별 사망자수"
        #     )
        # st.plotly_chart(fig1)    
        # fig2 = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "부상자수",
        #     title = "시군구별 부상자수"
        #     )
        # st.plotly_chart(fig2)  
        # fig3 = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "중상",
        #     title = "시군구별 중상"
        #     )
        # st.plotly_chart(fig3)     
        # fig4 = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "경상",
        #     title = "시군구별 경상"
        #     )
        # st.plotly_chart(fig4)    
        # fig5 = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "부상신고",
        #     title = "시군구별 부상신고"
        #     )
        # st.plotly_chart(fig5)
           
    elif now=='충북'  :
        df=df.loc[55:65,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
    elif now=='충남'  :
        df=df.loc[66:78,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
    elif now=='광주'  :
        df=df.loc[151:152,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
    elif now=='대전'  :
        df=df.loc[153:157,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
    elif now=='전북'  :     
        df=df.loc[92:105,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
    
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
    elif now=='전남'  :     
        df=df.loc[92:105,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
    
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
    elif now=='대구'  :     
        df=df.loc[137:142,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
    
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
    elif now=='부산'  :     
        df=df.loc[12:17,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
    
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
            df,
            x = "시군구",
            y = "부상자수",
            title = "시군구별 부상자수"
            )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
            df,
            x = "시군구",
            y = "부상신고",
            title = "시군구별 부상신고"
            )   
        st.plotly_chart(fig5) 
    elif now=='울산'  :     
        df={'발생건수':47,'사망자수':5,'부상자수':79,'중상':18,'경상':57,'부상신고':4}
        st.write(df)
        # df=df.loc[158,:]
        # fig = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "발생건수",
        #     title = "시군구별 발생건수"
        #     )
        # st.plotly_chart(fig)
    
        # fig1 = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "사망자수",
        #     title = "시군구별 사망자수"
        #     )
        # st.plotly_chart(fig1)    
        # fig2 = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "부상자수",
        #     title = "시군구별 부상자수"
        #     )
        # st.plotly_chart(fig2)  
        # fig3 = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "중상",
        #     title = "시군구별 중상"
        #     )
        # st.plotly_chart(fig3)     
        # fig4 = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "경상",
        #     title = "시군구별 경상"
        #     )
        # st.plotly_chart(fig4)    
        # fig5 = px.bar(        
        #     df,
        #     x = "시군구",
        #     y = "부상신고",
        #     title = "시군구별 부상신고"
        #     )   
        # st.plotly_chart(fig5) 
    elif now=='경북'  :     
        df=df.loc[106:122,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
    
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
        df,
        x = "시군구",
        y = "부상자수",
        title = "시군구별 부상자수"
        )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
        df,
        x = "시군구",
        y = "부상신고",
        title = "시군구별 부상신고"
        )   
        st.plotly_chart(fig5)
    elif now=='경남'  :     
        df=df.loc[123:136,:]
        fig = px.bar(        
            df,
            x = "시군구",
            y = "발생건수",
            title = "시군구별 발생건수"
            )
        st.plotly_chart(fig)
    
        fig1 = px.bar(        
            df,
            x = "시군구",
            y = "사망자수",
            title = "시군구별 사망자수"
            )
        st.plotly_chart(fig1)    
        fig2 = px.bar(        
        df,
        x = "시군구",
        y = "부상자수",
        title = "시군구별 부상자수"
        )
        st.plotly_chart(fig2)  
        fig3 = px.bar(        
            df,
            x = "시군구",
            y = "중상",
            title = "시군구별 중상"
            )
        st.plotly_chart(fig3)     
        fig4 = px.bar(        
            df,
            x = "시군구",
            y = "경상",
            title = "시군구별 경상"
            )
        st.plotly_chart(fig4)    
        fig5 = px.bar(        
        df,
        x = "시군구",
        y = "부상신고",
        title = "시군구별 부상신고"
        )   
        st.plotly_chart(fig5) 
        
        
        
        
         
           

   
  