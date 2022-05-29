import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#日本語文字化け対策でフォント指定
sns.set(font='Hiragino Sans')
plt.rcParams['font.family'] = "Hiragino Sans"

def app():

  st.title("トレーニング結果分析")

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
  
  st.caption("3つの選択色の関係性を見る　ー　col_3aを第一選択色として、col_3b, col_3cとの散布図を書く")
  
  ##愛らしい
  cdf_airashii = cdf[cdf['kwd'] == '愛らしい']
  #cdf_airashii

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_airashii['col_3a'], cdf_airashii['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_airashii['col_3a'], cdf_airashii['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q1：愛らしい")
  st.pyplot()


  ##楽しい
  cdf_tanoshii = cdf[cdf['kwd'] == '楽しい']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_tanoshii['col_3a'], cdf_tanoshii['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_tanoshii['col_3a'], cdf_tanoshii['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q2：楽しい")
  st.pyplot()
  
  
    ##豪華な
  cdf_goukana = cdf[cdf['kwd'] == '豪華な']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_goukana['col_3a'], cdf_goukana['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_goukana['col_3a'], cdf_goukana['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q3：豪華な")
  st.pyplot()
  
  
    ##素朴な
  cdf_sobokuna= cdf[cdf['kwd'] == '素朴な']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_sobokuna['col_3a'], cdf_sobokuna['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_sobokuna['col_3a'], cdf_sobokuna['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q4：素朴な")
  st.pyplot()
  
  
    ##味わい深い
  cdf_ajiwai = cdf[cdf['kwd'] == '味わい深い']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_ajiwai['col_3a'], cdf_ajiwai['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_ajiwai['col_3a'], cdf_ajiwai['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q5：味わい深い")
  st.pyplot()
  
  
    ##格調のある
  cdf_kakuchou = cdf[cdf['kwd'] == '格調のある']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_kakuchou['col_3a'], cdf_kakuchou['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_kakuchou['col_3a'], cdf_kakuchou['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q6：格調のある")
  st.pyplot()
  
  
    ##優雅な
  cdf_yuuga = cdf[cdf['kwd'] == '優雅な']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_yuuga['col_3a'], cdf_yuuga['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_yuuga['col_3a'], cdf_yuuga['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q7：優雅な")
  st.pyplot()
  
  
    ##気品のある
  cdf_kihin = cdf[cdf['kwd'] == '気品のある']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_kihin['col_3a'], cdf_kihin['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_kihin['col_3a'], cdf_kihin['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q8：気品のある")
  st.pyplot()
  
  
    ##合理的な
  cdf_gouriteki = cdf[cdf['kwd'] == '合理的な']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_gouriteki['col_3a'], cdf_gouriteki['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_gouriteki['col_3a'], cdf_gouriteki['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q9：合理的な")
  st.pyplot()
  
  
    ##favorite
  cdf_favorite = cdf[cdf['kwd'] == 'favorite']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_favorite ['col_3a'], cdf_favorite ['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_favorite ['col_3a'], cdf_favorite ['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q10：favorite")
  st.pyplot()
  
  
    ##春
  cdf_spring = cdf[cdf['kwd'] == '春']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_spring['col_3a'], cdf_spring['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_spring['col_3a'], cdf_spring['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q13：春")
  st.pyplot()
  
  
    ##夏
  cdf_summer = cdf[cdf['kwd'] == '夏']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_summer['col_3a'], cdf_summer['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_summer['col_3a'], cdf_summer['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q14：夏")
  st.pyplot()
  
  
    ##秋
  cdf_autumn = cdf[cdf['kwd'] == '秋']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_autumn['col_3a'], cdf_autumn['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_autumn['col_3a'], cdf_autumn['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q15：秋")
  st.pyplot()
  
  
    ##冬
  cdf_winter = cdf[cdf['kwd'] == '冬']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_winter['col_3a'], cdf_winter['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_winter['col_3a'], cdf_winter['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q16：冬")
  st.pyplot()
  
  
    ##朝
  cdf_morning = cdf[cdf['kwd'] == '朝']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_morning['col_3a'], cdf_morning['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_morning['col_3a'], cdf_morning['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q17：朝")
  st.pyplot()
  
  
    ##昼
  cdf_midday = cdf[cdf['kwd'] == '昼']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_midday['col_3a'], cdf_midday['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_midday['col_3a'], cdf_midday['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q18：昼")
  st.pyplot()
  
  
    ##夕
  cdf_evening = cdf[cdf['kwd'] == '夕']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_evening['col_3a'], cdf_evening['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_evening['col_3a'], cdf_evening['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q19：夕")
  st.pyplot()
  
    ##夜
  cdf_night = cdf[cdf['kwd'] == '夜']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_night['col_3a'], cdf_night['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_night['col_3a'], cdf_night['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subtitle("Q20：夜")
  st.pyplot()
