# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:04:16 2022

@author: Chandramouli
"""

import streamlit as st
import pandas as pd
import joblib
import pickle
import numpy as np





def load_pkl(name):
    model=joblib.load(name)
    return model

#def handle_click(day):
#    st.session_state.day=day


st.markdown("# TGV6109 Price Forecasting")
day_list=['150','120','90','75','60','45','30','15','10','7','6','3','2','1']
price=np.arange(0,2000)

day=st.selectbox("Type in the day for which price needs to be predicted",day_list)

if day not in st.session_state:
    st.session_state.day=day
##change=st.button('Change',  on_click=handle_click,  args=[day])
#st.write(st.session_state.day)


#day=6
if day=='1':
   
    #day_list=['180','150','120','90','75','60','45','30','15','10','7','6','3','2']
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)
    e=st.selectbox("75th day price",price)
    test.append(e)
    f=st.selectbox("60th day price",price)
    test.append(f)
    g=st.selectbox("45th day price",price)
    test.append(g)
    h=st.selectbox("30th day price",price)
    test.append(h)
    i=st.selectbox("15th day price",price)
    test.append(i)
    j=st.selectbox("10th day price",price)
    test.append(j)
    k=st.selectbox("7th day price",price)
    test.append(k)
    l=st.selectbox("6th day price",price)
    test.append(l)
    m=st.selectbox("3rd day price",price)
    test.append(m)
    n=st.selectbox("2nd day price",price)
    test.append(n)

    
    model_1=load_pkl("finalized_model_14.pkl")
    pred=model_1.predict([test])
    
    #st.success("The forecasted result for day 1 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 1 is {}".format(pred))
        
        

    
elif day=='2':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)
    e=st.selectbox("75th day price",price)
    test.append(e)
    f=st.selectbox("60th day price",price)
    test.append(f)
    g=st.selectbox("45th day price",price)
    test.append(g)
    h=st.selectbox("30th day price",price)
    test.append(h)
    i=st.selectbox("15th day price",price)
    test.append(i)
    j=st.selectbox("10th day price",price)
    test.append(j)
    k=st.selectbox("7th day price",price)
    test.append(k)
    l=st.selectbox("6th day price",price)
    test.append(l)
    m=st.selectbox("3rd day price",price)
    test.append(m)  
    model_2=load_pkl("finalized_model_13.pkl")
    pred=model_2.predict([test])
    
    #st.success("The forecasted result for day 2 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 2 is {}".format(pred))
    
    
elif day=='3':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)
    e=st.selectbox("75th day price",price)
    test.append(e)
    f=st.selectbox("60th day price",price)
    test.append(f)
    g=st.selectbox("45th day price",price)
    test.append(g)
    h=st.selectbox("30th day price",price)
    test.append(h)
    i=st.selectbox("15th day price",price)
    test.append(i)
    j=st.selectbox("10th day price",price)
    test.append(j)
    k=st.selectbox("7th day price",price)
    test.append(k)
    l=st.selectbox("6th day price",price)
    test.append(l)

    model_3=load_pkl("finalized_model_12.pkl")
    pred=model_3.predict([test])
    
    #st.success("The forecasted result for day 3 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 3 is {}".format(pred))
    
    
    
elif day=='6':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)
    e=st.selectbox("75th day price",price)
    test.append(e)
    f=st.selectbox("60th day price",price)
    test.append(f)
    g=st.selectbox("45th day price",price)
    test.append(g)
    h=st.selectbox("30th day price",price)
    test.append(h)
    i=st.selectbox("15th day price",price)
    test.append(i)
    j=st.selectbox("10th day price",price)
    test.append(j)
    k=st.selectbox("7th day price",price)
    test.append(k)

    model_6=load_pkl("finalized_model_11.pkl")
    pred=model_6.predict([test])
    
    #st.success("The forecasted result for day 6 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 6 is {}".format(pred))
    
    
    
elif day=='7':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)
    e=st.selectbox("75th day price",price)
    test.append(e)
    f=st.selectbox("60th day price",price)
    test.append(f)
    g=st.selectbox("45th day price",price)
    test.append(g)
    h=st.selectbox("30th day price",price)
    test.append(h)
    i=st.selectbox("15th day price",price)
    test.append(i)
    j=st.selectbox("10th day price",price)
    test.append(j)


    model_7=load_pkl("finalized_model_10.pkl")
    pred=model_7.predict([test])
    
    #st.success("The forecasted result for day 7 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 7 is {}".format(pred))

    
elif day=='10':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)
    e=st.selectbox("75th day price",price)
    test.append(e)
    f=st.selectbox("60th day price",price)
    test.append(f)
    g=st.selectbox("45th day price",price)
    test.append(g)
    h=st.selectbox("30th day price",price)
    test.append(h)
    i=st.selectbox("15th day price",price)
    test.append(i)
 

    model_10=load_pkl("finalized_model_9.pkl")
    pred=model_10.predict([test])
    
    #st.success("The forecasted result for day 10 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 10 is {}".format(pred))


elif day=='15':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)
    e=st.selectbox("75th day price",price)
    test.append(e)
    f=st.selectbox("60th day price",price)
    test.append(f)
    g=st.selectbox("45th day price",price)
    test.append(g)
    h=st.selectbox("30th day price",price)
    test.append(h)
   
 

    model_15=load_pkl("finalized_model_8.pkl")
    pred=model_15.predict([test])
    
    #st.success("The forecasted result for day 15 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 15 is {}".format(pred))


elif day=='30':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)
    e=st.selectbox("75th day price",price)
    test.append(e)
    f=st.selectbox("60th day price",price)
    test.append(f)
    g=st.selectbox("45th day price",price)
    test.append(g)
   
   
 

    model_30=load_pkl("finalized_model_7.pkl")
    pred=model_30.predict([test])
    
    #st.success("The forecasted result for day 30 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 30 is {}".format(pred))


elif day=='45':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)
    e=st.selectbox("75th day price",price)
    test.append(e)
    f=st.selectbox("60th day price",price)
    test.append(f)
 
   
 

    model_45=load_pkl("finalized_model_6.pkl")
    pred=model_45.predict([test])
    
    #st.success("The forecasted result for day 45 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 45 is {}".format(pred))
    
    
elif day=='60':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)
    e=st.selectbox("75th day price",price)
    test.append(e)
  
   
 

    model_60=load_pkl("finalized_model_5.pkl")
    pred=model_60.predict([test])
    
    #st.success("The forecasted result for day 60 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 60 is {}".format(pred))
    
elif day=='75':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)
    d=st.selectbox("90th day price",price)
    test.append(d)

    model_75=load_pkl("finalized_model_4.pkl")
    pred=model_75.predict([test])
    
    #st.success("The forecasted result for day 75 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 75 is {}".format(pred))
    
elif day=='90':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)
    c=st.selectbox("120th day price",price)
    test.append(c)

    model_90=load_pkl("finalized_model_3.pkl")
    pred=model_90.predict([test])
    
    #st.success("The forecasted result for day 90 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 90 is {}".format(pred))
    
elif day=='120':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
    b=st.selectbox("150th day price",price)
    test.append(b)

    model_120=load_pkl("finalized_model_2.pkl")
    pred=model_120.predict([test])
    
    #st.success("The forecasted result for day 120 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 120 is {}".format(pred))
    
elif day=='150':
    test=[]
    a=st.selectbox("180th day price",price)
    test.append(a)
 
    model_150=load_pkl("finalized_model_1.pkl")
    pred=model_150.predict([test])
    
    #st.success("The forecasted result for day 150 is {}".format(pred))
    if st.button('Show Forecasting'):
        st.success("The forecasted result for day 150 is {}".format(pred))
    
    
#st.write(st.session_state)
