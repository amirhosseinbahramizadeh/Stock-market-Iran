import streamlit as st
import time
import numpy as np
import pandas as pd
import pytse_client as tse
from pytse_client import download_client_types_records

st.title("my project")
st.write("New Project ;")
add_selectbox = st.sidebar.selectbox(
    'شرکت مورد نظر را انتخاب کنید',
    ('وبملت','ولملت','پرشیا','جم','ثتران','پکویر','دانا')
)
if (add_selectbox == 'وبملت'):
    tse.download(symbols="وبملت", write_to_csv=True)  # optional
    ticker = tse.Ticker("وبملت")


if(add_selectbox == 'ولملت'):
    tse.download(symbols="ولملت", write_to_csv=True)  # optional
    ticker = tse.Ticker("ولملت")

if(add_selectbox == 'جم'):
    tse.download(symbols="جم", write_to_csv=True)  # optional
    ticker = tse.Ticker("جم")

if(add_selectbox == 'پکویر'):
    tse.download(symbols="پکویر", write_to_csv=True)  # optional
    ticker = tse.Ticker("پکویر")

if(add_selectbox == 'پرشیا'):
    tse.download(symbols="پرشیا", write_to_csv=True)  # optional
    ticker = tse.Ticker("پرشیا")

if(add_selectbox == 'دانا'):
    tse.download(symbols="دانا", write_to_csv=True)  # optional
    ticker = tse.Ticker("دانا")

if(add_selectbox == 'ثتران'):
    tse.download(symbols="ثتران", write_to_csv=True)  # optional
    ticker = tse.Ticker("ثتران")

left_column, right_column = st.beta_columns(2)
# You can use a column just like st.sidebar:
left_column.button('اطلاعات بورس بروزرسانی')


st.subheader("نام شرکت")
st.write(ticker.title)  # نام شرکت
st.subheader("آدرس صفحه سهم")
st.write(ticker.url)  # آدرس صفحه سهم
st.subheader("نام گروه")
st.write(ticker.group_name)  # نام گروه
st.subheader("eps")
st.write(ticker.eps)  # eps
st.subheader("P/E")
st.write(ticker.p_e_ratio)  # P/E
st.subheader("group P/E")
st.write(ticker.group_p_e_ratio)  # group P/E
st.subheader("حجم مبنا")
st.write(ticker.base_volume)  # حجم مبنا
st.subheader("آخرین معامله")
st.write(ticker.last_price)  # آخرین معامله
st.subheader("قیمت پایانی")
st.write(ticker.adj_close)  # قیمت پایانی
st.subheader("قیمت بهترین تقاضا")
st.write(ticker.best_supply_price)  # قیمت بهترین تقاضا
st.subheader("حجم بهترین تقاضا")
st.write(ticker.best_supply_vol)  # حجم بهترین تقاضا
st.subheader("تمام سهامداران")
st.write(ticker.shareholders.percentage.sum())
st.subheader("قیمت بهترین عرضه")
st.write(ticker.best_demand_price)  # قیمت بهترین عرضه
st.subheader("حجم بهترین عرضه")
st.write(ticker.best_demand_vol)  # حجم بهترین عرضه
st.subheader("اطلاعات سهام داران عمده")
st.write(ticker.shareholders)  # اطلاعات سهام داران عمده
st.subheader("سابقه قیمت سهم")
st.write(ticker.history)  # سابقه قیمت سهم
st.subheader("حقیقی حقوقی")
st.write(ticker.client_types)  # حقیقی حقوقی
