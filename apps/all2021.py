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
  
    #カラーチップを表示        
  st.image("color_chip156.jpeg", caption='色彩コード変換表(dummy)')

  #トップ選択色時に一緒に選択された第二、第三選択色の数をkwdごとにカウントした表
  cdf = pd.read_csv("col3.csv")
  #データ型を確認
  cdf.dtypes
  #　欠損値の確認
  cdf.isnull().any()
  cdf.isnull().sum()
  #欠損値を削除（nation, countryのデータ)
  cdf = cdf.dropna()

  st.caption("①t検定　ー　クラス間の差異を確認")
  st.caption("②パレート図　ー　色構成を見る")
  #kwd個別に切り出して可視化していく　
  
  

  #箱ひげ図で全体の散らばりを見る
  sns.catplot(data=df2, x="col_3a", y="kwd", kind="box",height=10, aspect=1.5, palette="coolwarm")
  st.subheader("1〜156の選択色のキーワードごとの集中度")
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.pyplot()
  st.caption("*縦軸は選択色の番号")

  #ヒートマップで全体の散らばりを見る
  sns.displot(data=df2, x="col_3a", y="kwd",height=10, aspect=1.5)
  st.subheader("同様に濃淡で示す")
  st.pyplot()


  
  st.caption("③3つの選択色の関係性を見る　ー　col_3aを第一選択色として、col_3b, col_3cとの散布図を書く")
  
  ##愛らしい
  cdf_airashii = cdf[cdf['kwd'] == 'lovely']
  #cdf_airashii

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_airashii['col_3a'], cdf_airashii['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_airashii['col_3a'], cdf_airashii['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q1：愛らしい")
  st.pyplot()


  ##楽しい
  cdf_tanoshii = cdf[cdf['kwd'] == 'fun']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_tanoshii['col_3a'], cdf_tanoshii['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_tanoshii['col_3a'], cdf_tanoshii['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q2：楽しい")
  st.pyplot()
  
  
    ##豪華な
  cdf_goukana = cdf[cdf['kwd'] == 'gorgeous']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_goukana['col_3a'], cdf_goukana['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_goukana['col_3a'], cdf_goukana['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q3：豪華な")
  st.pyplot()
  
  
    ##素朴な
  cdf_sobokuna= cdf[cdf['kwd'] == 'simple']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_sobokuna['col_3a'], cdf_sobokuna['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_sobokuna['col_3a'], cdf_sobokuna['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q4：素朴な")
  st.pyplot()
  
  
    ##味わい深い
  cdf_ajiwai = cdf[cdf['kwd'] == 'tasteful']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_ajiwai['col_3a'], cdf_ajiwai['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_ajiwai['col_3a'], cdf_ajiwai['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q5：味わい深い")
  st.pyplot()
  
  
    ##格調のある
  cdf_kakuchou = cdf[cdf['kwd'] == 'dignified']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_kakuchou['col_3a'], cdf_kakuchou['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_kakuchou['col_3a'], cdf_kakuchou['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q6：格調のある")
  st.pyplot()
  
  
    ##優雅な
  cdf_yuuga = cdf[cdf['kwd'] == 'graceful']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_yuuga['col_3a'], cdf_yuuga['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_yuuga['col_3a'], cdf_yuuga['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q7：優雅な")
  st.pyplot()
  
  
    ##気品のある
  cdf_kihin = cdf[cdf['kwd'] == 'elegant']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_kihin['col_3a'], cdf_kihin['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_kihin['col_3a'], cdf_kihin['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q8：気品のある")
  st.pyplot()
  
  
    ##合理的な
  cdf_gouriteki = cdf[cdf['kwd'] == 'reasonable']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_gouriteki['col_3a'], cdf_gouriteki['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_gouriteki['col_3a'], cdf_gouriteki['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q9：合理的な")
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
  st.subheader("Q10：favorite")
  st.pyplot()
  
  
    ##春
  cdf_spring = cdf[cdf['kwd'] == 'spring']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_spring['col_3a'], cdf_spring['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_spring['col_3a'], cdf_spring['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q13：春")
  st.pyplot()
  
  
    ##夏
  cdf_summer = cdf[cdf['kwd'] == 'summer']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_summer['col_3a'], cdf_summer['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_summer['col_3a'], cdf_summer['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q14：夏")
  st.pyplot()
  
  
    ##秋
  cdf_autumn = cdf[cdf['kwd'] == 'autumn']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_autumn['col_3a'], cdf_autumn['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_autumn['col_3a'], cdf_autumn['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q15：秋")
  st.pyplot()
  
  
    ##冬
  cdf_winter = cdf[cdf['kwd'] == 'winter']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_winter['col_3a'], cdf_winter['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_winter['col_3a'], cdf_winter['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q16：冬")
  st.pyplot()
  
  
    ##朝
  cdf_morning = cdf[cdf['kwd'] == 'morning']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_morning['col_3a'], cdf_morning['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_morning['col_3a'], cdf_morning['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q17：朝")
  st.pyplot()
  
  
    ##昼
  cdf_midday = cdf[cdf['kwd'] == 'midday']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_midday['col_3a'], cdf_midday['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_midday['col_3a'], cdf_midday['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q18：昼")
  st.pyplot()
  
  
    ##夕
  cdf_evening = cdf[cdf['kwd'] == 'sunset']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_evening['col_3a'], cdf_evening['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_evening['col_3a'], cdf_evening['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q19：夕")
  st.pyplot()
  
    ##夜
  cdf_night = cdf[cdf['kwd'] == 'night']

  #col_3aの選択色を第一選択色として、col_3b, col_3cとの関連を見るために散布図を書く
  plt.scatter(cdf_night['col_3a'], cdf_night['col_3b'], label='col_3b', color='blue')
  plt.scatter(cdf_night['col_3a'], cdf_night['col_3c'], label='col_3c', color='green')
  plt.xlabel('col_3a')
  plt.ylabel("col_3b & col_3c")
  plt.legend()
  plt.show()
  st.subheader("Q20：夜")
  st.pyplot()
