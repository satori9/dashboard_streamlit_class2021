import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import streamlit as st
import math

#日本語文字化け対策でフォント指定
sns.set(font='Hiragino Sans')
plt.rcParams['font.family'] = "Hiragino Sans"

st.title("analysis")

#トップ選択色時に一緒に選択された第二、第三選択色の数をkwdごとにカウントした表
cdf = pd.read_csv("col3.csv")
#データ型を確認
cdf.dtypes
#　欠損値の確認
cdf.isnull().any()
cdf.isnull().sum()
#欠損値を削除（nation, countryのデータ)
cdf = cdf.dropna()

#kwd個別に切り出して可視化していく
cdf_airashii = cdf[cdf['kwd'] == '愛らしい']
#cdf_airashii

#col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
plt.scatter(cdf_airashii['col_3a'], cdf_airashii['col_3b'], label='col_3b', color='blue')
plt.scatter(cdf_airashii['col_3a'], cdf_airashii['col_3c'], label='col_3c', color='green')
plt.xlabel('col_3a')
plt.ylabel("col_3b & col_3c")
plt.legend()
plt.show()

