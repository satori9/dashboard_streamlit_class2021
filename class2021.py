import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
#import japanize_matplotlib　 -入れてみたが「認識できない」エラーが出る

#日本語文字化け対策でフォント指定　　-！! Web表示すると効かないエラー
sns.set(font='Yu Gothic')
plt.rcParams['font.family'] = "Yu Gothic"

st.title("2021年度色彩トレーニング結果")


#2021年のクラス分をクレンジングしたデータ
df = pd.read_csv("class_2021.csv")
#欠損値を０で補う
df.fillna('FILL')
df['col_sum'] = df['col_sum'].fillna(0).astype('int64')


#下準備データ -ひとまずexpanderでラッピング。本来は非表示にしたい。
with st.expander("show data"):
    with st.form(key='data', clear_on_submit=True):
        
        #クロス集計の準備：col_sum列のカンマ区切りのデータを分割
        kwd = df['kwd'].map(lambda x: x.split(','))
        #numpy.arrayにして二次元から一次元のデータに変換
        ser = pd.Series(np.hstack(kwd.values))
        #ユニークにする
        unique_kwd = ser.str.strip().unique()
        unique_kwd.sort()
        unique_kwd

        #指定したkwdをDataframeから抽出
        def filter_df_by_kwd(df, kwd):
            kwd_df = df.loc[df['kwd'].map(lambda x: kwd in x)].copy()
            kwd_df['kwd'] = kwd
            return kwd_df

        #上記の関数を全てのkwdに対して実行
        kwd_df_list = [filter_df_by_kwd(df, kwd) for kwd in unique_kwd]
        #上記dataを統合
        df2 = pd.concat(kwd_df_list)
        #col_sum列でソート
        df2.sort_values('col_sum', inplace=True)

        #kwd列とcol_sum列のクロス集計
        df2.pivot_table(index='kwd', columns='col_sum', values='count', aggfunc=np.sum)
        
        """
-!効いてない
#選択色番号の色変換データ
cdf = pd.read_csv('ColorChip156.csv', encoding="cp932")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
cdf[["num", "#323200"]]

def color_num(col_sum):
  if col_sum == 1:
    return '#FFFFFF'
  elif col_sum == 2:
    return '#FFE8E8'
  elif col_sum == 3:
    return '#FFF5E7'
  elif col_sum == 4:
    return '#FFFAE7'
  elif col_sum == 5:
    return '#FFFFE7'
  elif col_sum == 6:
    return '#F8FFE7'
  elif col_sum == 7:
    return '#E9FFE7'
  elif col_sum == 8:
    return '#E7FBFF'
  elif col_sum == 9:
    return '#E8F4FF'
  elif col_sum == 10:
    return '#E8EAFF'
  elif col_sum == 11:
    return '#F6E7FF'
  elif col_sum == 12:
    return '#FFE8F6'
  elif col_sum == 13:
    return '#FFFFFF'
  elif col_sum == 14:
    return '#FFB9B8'
  elif col_sum == 15:
    return '#FFD4B7'
  elif col_sum == 16:
    return '#FFE2B7'
  elif col_sum == 17:
    return '#FFF1B6'
  elif col_sum == 18:
    return '#FFFFB5'
  elif col_sum == 19:
    return '#EAFFB6'
  elif col_sum == 20:
    return '#BDFFB6'
  elif col_sum == 21:
    return '#FFE8E8'
  elif col_sum == 22:
    return '#B8DEFF'
  elif col_sum == 23:
    return '#B9BFFF'
  elif col_sum == 24:
    return '#E4B7FF'
  elif col_sum == 25:
    return '#FFB8E6'
  elif col_sum == 26:
    return '#DBDBDB'
  elif col_sum == 27:
    return '#FF8A89'
  elif col_sum == 28:
    return '#FFB887'
  elif col_sum == 29:
    return '#FFCE86'
  elif col_sum == 30:
    return '#FFE785'
  elif col_sum == 31:
    return '#FFFF83'
  elif col_sum == 32:
    return '#DBFF84'
  elif col_sum == 33:
    return '#91FF85'
  elif col_sum == 34:
    return '#87EAFF'
  elif col_sum == 35:
    return '#88C8FF'
  elif col_sum == 36:
    return '#8A94FF'
  elif col_sum == 37:
    return '#D287FF'
  elif col_sum == 38:
    return '#FF88D5'
  elif col_sum == 39:
    return '#B2B2B2'
  elif col_sum == 40:
    return '#FF5B59'
  elif col_sum == 41:
    return '#FF9B56'
  elif col_sum == 42:
    return '#FFB954'
  elif col_sum == 43:
    return '#FFDD50'
  elif col_sum == 44:
    return '#FFFF4C'
  elif col_sum == 45:
    return '#CDFF4E'
  elif col_sum == 46:
    return '#63FF51'
  elif col_sum == 47:
    return '#55E1FF'
  elif col_sum == 48:
    return '#58B1FF'
  elif col_sum == 49:
    return '#5B68FF'
  elif col_sum == 50:
    return '#BF55FF'
  elif col_sum == 51:
    return '#FF58C4'
  elif col_sum == 52:
    return '#a6a6a6'
  elif col_sum == 53:
    return '#FF2A22'
  elif col_sum == 54:
    return '#FF7F1A'
  elif col_sum == 55:
    return '#FFA511'
  elif col_sum == 56:
    return '#FFD300'
  elif col_sum == 57:
    return '#FFFF26'
  elif col_sum == 58:
    return '#BEFF00'
  elif col_sum == 59:
    return '#2EFF00'
  elif col_sum == 60:
    return '#17D9FF'
  elif col_sum == 61:
    return '#239CFF'
  elif col_sum == 62:
    return '#2A37FF'
  elif col_sum == 63:
    return '#AD15FF'
  elif col_sum == 64:
    return '#FF21B3'
  elif col_sum == 65:
    return '#999999'
  elif col_sum == 66:
    return '#FF0000'
  elif col_sum == 67:
    return '#FF6100'
  elif col_sum == 68:
    return '#FF9000'
  elif col_sum == 69:
    return '#FFC900'
  elif col_sum == 70:
    return '#FFFF00'
  elif col_sum == 71:
    return '#B1FF00'
  elif col_sum == 72:
    return '#00FF00'
  elif col_sum == 73:
    return '#00CFFF'
  elif col_sum == 74:
    return '#0085FF'
  elif col_sum == 75:
    return '#0000FF'
  elif col_sum == 76:
    return '#9B00FF'
  elif col_sum == 77:
    return '#FF00A2'
  elif col_sum == 78:
    return '#7F7F7F'
  elif col_sum == 79:
    return '#D30000'
  elif col_sum == 80:
    return '#D35000'
  elif col_sum == 81:
    return '#D37600'
  elif col_sum == 82:
    return '#D2A500'
  elif col_sum == 83:
    return '#D1D300'
  elif col_sum == 84:
    return '#90D300'
  elif col_sum == 85:
    return '#00D300'
  elif col_sum == 86:
    return '#00A9D3'
  elif col_sum == 87:
    return '#006CD4'
  elif col_sum == 88:
    return '#0000D5'
  elif col_sum == 89:
    return '#7F00D4'
  elif col_sum == 90:
    return '#D30085'
  elif col_sum == 91:
    return '#656565'
  elif col_sum == 92:
    return '#A40000'
  elif col_sum == 93:
    return '#A43E00'
  elif col_sum == 94:
    return '#FFE8E8'
  elif col_sum == 94:
    return '#A35C00'
  elif col_sum == 95:
    return '#A38000'
  elif col_sum == 96:
    return '#A2A300'
  elif col_sum == 97:
    return '#71A300'
  elif col_sum == 98:
    return '#00A400'
  elif col_sum == 99:
    return '#0084A4'
  elif col_sum == 100:
    return '#0055A4'
  elif col_sum == 101:
    return '#0000A5'
  elif col_sum == 102:
    return '#6300A5'
  elif col_sum == 103:
    return '#A40066'
  elif col_sum == 104:
    return '#4C4C4C'
  elif col_sum == 105:
    return '#750000'
  elif col_sum == 106:
    return '#752D00'
  elif col_sum == 107:
    return '#754100'
  elif col_sum == 108:
    return '#755C00'
  elif col_sum == 109:
    return '#747500'
  elif col_sum == 110:
    return '#507500'
  elif col_sum == 111:
    return '#007500'
  elif col_sum == 112:
    return '#005F75'
  elif col_sum == 113:
    return '#003C76'
  elif col_sum == 114:
    return '#000276'
  elif col_sum == 115:
    return '#460076'
  elif col_sum == 116:
    return '#750049'
  elif col_sum == 117:
    return '#404040'
  elif col_sum == 118:
    return '#650000'
  elif col_sum == 119:
    return '#651900'
  elif col_sum == 120:
    return '#653200'
  elif col_sum == 121:
    return '#654c00'
  elif col_sum == 122:
    return '#656500'
  elif col_sum == 123:
    return '#4c6500'
  elif col_sum == 124:
    return '#006500'
  elif col_sum == 125:
    return '#004c65'
  elif col_sum == 126:
    return '#003265'
  elif col_sum == 127:
    return '#000065'
  elif col_sum == 128:
    return '#320065'
  elif col_sum == 129:
    return '#650032'
  elif col_sum == 130:
    return '#323232'
  elif col_sum == 131:
    return '#470000'
  elif col_sum == 132:
    return '#471B00'
  elif col_sum == 133:
    return '#472700'
  elif col_sum == 134:
    return '#463700'
  elif col_sum == 135:
    return '#464700'
  elif col_sum == 136:
    return '#304700'
  elif col_sum == 137:
    return '#014700'
  elif col_sum == 138:
    return '#003947'
  elif col_sum == 139:
    return '#002447'
  elif col_sum == 140:
    return '#000347'
  elif col_sum == 141:
    return '#2A0047'
  elif col_sum == 142:
    return '#47002C'
  elif col_sum == 143:
    return '#191919'
  elif col_sum == 144:
    return '#320000'
  elif col_sum == 145:
    return '#320c00'
  elif col_sum == 146:
    return '#321900'
  elif col_sum == 147:
    return '#322600'
  elif col_sum == 148:
    return '#323200'
  elif col_sum == 149:
    return '#263200'
  elif col_sum == 150:
    return '#003200'
  elif col_sum == 151:
    return '#003232'
  elif col_sum == 152:
    return '#002632'
  elif col_sum == 153:
    return '#000032'
  elif col_sum == 154:
    return '#260032'
  elif col_sum == 155:
    return '#320026'
  elif col_sum == 156:
    return '#000000'
  else:
    return '#000000'
"""

"""
選択色を番号順で並べ、選択した数の総計をバーチャートで可視化 -!全部黒になってしまうエラー中
df_airashii_count.plot.bar(by=["col_sum", "count"], color=list(map(color_num, "col_sum")), xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);
for i in map(color_num, "col_sum"):
    print(i)
"""
        
#streamlitでの表示データのフィルタリング（まだ未装。とりあえず１を手動で作成。集計→表示を自動化できないと辛い。）
choose_id = st.selectbox("表示するデータを選択して下さい", (
        "ALL", "1"))
#choose_id = st.selectbox('Choose ID', df2, help = 'Filter report to show only one')

if choose_id == '1':
    st.write('1の結果を表示')
if choose_id == 'ALL':
    st.write('ALLの結果を表示')
    

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



#kwd個別に切り出して可視化していく
#!愛らしい
df_airashii = df[df['kwd'] == '(1) 愛らしい']

#愛らしいの選択色の集計
df_airashii_count = df_airashii[['count',"col_sum"]].groupby("col_sum").count()

#選択色を番号順で並べ、選択した数の総計をバーチャートで可視化
df_airashii_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);




#streamlit表示
st.header("Q1：愛らしい")
st.bar_chart(df_airashii_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）       
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q1-1', '#FFB8E6')
    st.write(color)

with col2:
    color = st.color_picker('Q1-2', '#FFE8F6')
    st.write(color)

with col3:
    color = st.color_picker('Q1-3', '#FF88D5')
    st.write(color)

with col4:
    color = st.color_picker('Q1-4', '#FFB9B8')
    st.write(color)

with col5:
    color = st.color_picker('Q1-5', '#FF58C4')
    st.write(color)

#1選択時に追加で表示（とりあえずテスト。本当は自動化したい）
if choose_id == '1':
        st.subheader("あなたの選択した３色")   
        col1, col2, col3 = st.columns(3)
       
        with col1:
            color = st.color_picker('Q1-1', '#FFFFFF')
            st.write(color)

        with col2:
            color = st.color_picker('Q1_2', '#FFB8E6')
            st.write(color)

        with col3:
            color = st.color_picker('Q1-3', '#FFE8E8')
            st.write(color)

    
#!楽しい   
df_tanoshii = df[df['kwd'] == '(2) 楽しい']

#選択色の集計
df_tanoshii_count = df_tanoshii[['count',"col_sum"]].groupby("col_sum").count()

df_tanoshii_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

#streamlit表示
st.header("Q2：楽しい")
st.bar_chart(df_tanoshii_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q2-1', '#FFFF26')
    st.write(color)

with col2:
    color = st.color_picker('Q2-2', '#FFFF00')
    st.write(color)

with col3:
    color = st.color_picker('Q2-3', '#FF6100')
    st.write(color)

with col4:
    color = st.color_picker('Q2-4', '#FFB954')
    st.write(color)

with col5:
    color = st.color_picker('Q2-5', '#FFA511')
    st.write(color)
    
    
#!(3) 豪華な
df_goukana = df[df['kwd'] == '(3) 豪華な']

df_goukana_count = df_goukana[['count',"col_sum"]].groupby("col_sum").count()

df_goukana_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q3：豪華な")
st.bar_chart(df_goukana_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q3-1', '#FF0000')
    st.write(color)
with col2:
    color = st.color_picker('Q3-2', '#FFFF00')
    st.write(color)
with col3:
    color = st.color_picker('Q3-3', '#FF00A2')
    st.write(color)
with col4:
    color = st.color_picker('Q3-4', '#000000')
    st.write(color)
with col5:
    color = st.color_picker('Q3-5', '#FFFF26')
    st.write(color)

    
    
#!(4) 素朴な
df_sobokuna = df[df['kwd'] == '(4) 素朴な']

df_sobokuna_count = df_sobokuna[['count',"col_sum"]].groupby("col_sum").count()

df_sobokuna_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q4：素朴な")
st.bar_chart(df_sobokuna_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q4-1', '#DBDBDB')
    st.write(color)
with col2:
    color = st.color_picker('Q4-2', '#463700')
    st.write(color)
with col3:
    color = st.color_picker('Q4-3', '#FFF1E7')
    st.write(color)
with col4:
    color = st.color_picker('Q4-4', '#FFFFFF')
    st.write(color)
with col5:
    color = st.color_picker('Q4-5', '#656565')
    st.write(color)
    


#!(5) 味わい深い'
df_ajiwai = df[df['kwd'] == '(5) 味わい深い']

df_ajiwai_count = df_ajiwai[['count',"col_sum"]].groupby("col_sum").count()

df_ajiwai_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q5：味わい深い")
st.bar_chart(df_ajiwai_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q5-1', '#656565')
    st.write(color)
with col2:
    color = st.color_picker('Q5-2', '#A2A300')
    st.write(color)
with col3:
    color = st.color_picker('Q5-3', '#D35000')
    st.write(color)
with col4:
    color = st.color_picker('Q5-4', '#650000')
    st.write(color)
with col5:
    color = st.color_picker('Q5-5', '#003232')
    st.write(color)
    
    
#!(6) 格調のある
df_kakuchou = df[df['kwd'] == '(6) 格調のある']

df_kakuchou_count = df_kakuchou[['count',"col_sum"]].groupby("col_sum").count()

df_kakuchou_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q6：格調のある")
st.bar_chart(df_kakuchou_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q6-1', '#FFFF00')
    st.write(color)
with col2:
    color = st.color_picker('Q6-2', '#D1D300')
    st.write(color)
with col3:
    color = st.color_picker('Q6-3', '#650000')
    st.write(color)
with col4:
    color = st.color_picker('Q6-4', '#A40000')
    st.write(color)
with col5:
    color = st.color_picker('Q6-5', '#D30000')
    st.write(color)
    

          
#!(7) 優雅な
df_yuuga = df[df['kwd'] == '(7) 優雅な']

df_yuuga_count = df_yuuga[['count',"col_sum"]].groupby("col_sum").count()

df_yuuga_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q7：優雅な")
st.bar_chart(df_yuuga_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q7-1', '#A40066')
    st.write(color)
with col2:
    color = st.color_picker('Q7-2', '#FFFFFF')
    st.write(color)
with col3:
    color = st.color_picker('Q7-3', '#E4B7FF')
    st.write(color)
with col4:
    color = st.color_picker('Q7-4', '#87EAFF')
    st.write(color)
with col5:
    color = st.color_picker('Q7-5', '#750000')
    st.write(color)
    

          
#!(8) 気品のある
df_kihin = df[df['kwd'] == '(8) 気品のある']

df_kihin_count = df_kihin[['count',"col_sum"]].groupby("col_sum").count()

df_kihin_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q8：気品のある")
st.bar_chart(df_kihin_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q8-1', '#FFFFFF')
    st.write(color)
with col2:
    color = st.color_picker('Q8-2', '#750049')
    st.write(color)
with col3:
    color = st.color_picker('Q8-3', '#460076')
    st.write(color)
with col4:
    color = st.color_picker('Q8-4', '#BF55FF')
    st.write(color)
with col5:
    color = st.color_picker('Q8-5', '#000000')
    st.write(color)    


#!(9) 合理的な
df_gouriteki = df[df['kwd'] == '(9) 合理的な']

df_gouriteki_count = df_gouriteki[['count',"col_sum"]].groupby("col_sum").count()

df_gouriteki_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q9：合理的な")
st.bar_chart(df_gouriteki_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q9-1', '#0000D5')
    st.write(color)
with col2:
    color = st.color_picker('Q9-2', '#000000')
    st.write(color)
with col3:
    color = st.color_picker('Q9-3', '#FF2A22')
    st.write(color)
with col4:
    color = st.color_picker('Q9-4', '#FFFFFF')
    st.write(color)
with col5:
    color = st.color_picker('Q9-5', '#FFFF00')
    st.write(color)    


    
#!'favorite'
df_favorite = df[df['kwd'] == 'favorite']

df_favorite_count = df_favorite[['count',"col_sum"]].groupby("col_sum").count()

df_favorite_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q10：favorite")
st.bar_chart(df_favorite_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q10-1', '#FFB8E6')
    st.write(color)
with col2:
    color = st.color_picker('Q10-2', '#FFFFFF')
    st.write(color)
with col3:
    color = st.color_picker('Q10-3', '#000000')
    st.write(color)
with col4:
    color = st.color_picker('Q10-4', '#E4B7FF')
    st.write(color)
with col5:
    color = st.color_picker('Q10-5', '#55E1FF')
    st.write(color) 


          
#!'hometown'
df_hometown = df[df['kwd'] == 'hometown']

df_hometown_count = df_hometown[['count',"col_sum"]].groupby("col_sum").count()

df_hometown_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q11：hometown")
st.bar_chart(df_hometown_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q11-1', '#007500')
    st.write(color)
with col2:
    color = st.color_picker('Q11-2', '#00A400')
    st.write(color)
with col3:
    color = st.color_picker('Q11-3', '#00A400')
    st.write(color)
with col4:
    color = st.color_picker('Q11-4', '#D30000')
    st.write(color)
with col5:
    color = st.color_picker('Q11-5', '#91FF85')
    st.write(color) 

    

#!'nation'
df_nation = df[df['kwd'] == 'nation']

df_nation_count = df_nation[['count',"col_sum"]].groupby("col_sum").count()

df_nation_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q12：nation")
st.bar_chart(df_nation_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q12-1', '#FF0000')
    st.write(color)
with col2:
    color = st.color_picker('Q12-2', '#FFFFFF')
    st.write(color)
with col3:
    color = st.color_picker('Q12-3', '#D30000')
    st.write(color)
with col4:
    color = st.color_picker('Q12-4', '#A40000')
    st.write(color)
with col5:
    color = st.color_picker('Q12-5', '#FF88D5')
    st.write(color) 


    
#!春(spring)
df_spring = df[df['kwd'] == '春(spring)']

df_spring_count = df_spring[['count',"col_sum"]].groupby("col_sum").count()

df_spring_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q13：春(spring)")
st.bar_chart(df_spring_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q13-1', '#FFB8E6')
    st.write(color)
with col2:
    color = st.color_picker('Q13-2', '#FFE8F6')
    st.write(color)
with col3:
    color = st.color_picker('Q13-3', '#FFFFB5')
    st.write(color)
with col4:
    color = st.color_picker('Q13-4', '#FFB9B8')
    st.write(color)
with col5:
    color = st.color_picker('Q13-5', '#BDFFB6')
    st.write(color) 
    
    

#!夏(summer)
df_summer = df[df['kwd'] == '夏(summer)']

df_summer_count = df_spring[['count',"col_sum"]].groupby("col_sum").count()

df_summer_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q14：夏(summer)")
st.bar_chart(df_summer_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q14-1', '#FFFF00')
    st.write(color)
with col2:
    color = st.color_picker('Q14-2', '#00CFFF')
    st.write(color)
with col3:
    color = st.color_picker('Q14-3', '#17D9FF')
    st.write(color)
with col4:
    color = st.color_picker('Q14-4', '#55E1FF')
    st.write(color)
with col5:
    color = st.color_picker('Q14-5', '#FF0000')
    st.write(color) 
    
    

#!秋(autumn)
df_autumn = df[df['kwd'] == '秋(autumn)']

df_autumn_count = df_autumn[['count',"col_sum"]].groupby("col_sum").count()

df_autumn_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q15：秋(autumn)")
st.bar_chart(df_autumn_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q15-1', '#A35C00')
    st.write(color)
with col2:
    color = st.color_picker('Q15-2', '#D37600')
    st.write(color)
with col3:
    color = st.color_picker('Q15-3', '#A43E00')
    st.write(color)
with col4:
    color = st.color_picker('Q15-4', '#750000')
    st.write(color)
with col5:
    color = st.color_picker('Q15-5', '#755C00')
    st.write(color) 
     
    

#!冬(winter)
df_winter = df[df['kwd'] == '冬(winter)']

df_winter_count = df_winter[['count',"col_sum"]].groupby("col_sum").count()

df_winter_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q16：冬(winter)")
st.bar_chart(df_winter_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q16-1', '#FFFFFF')
    st.write(color)
with col2:
    color = st.color_picker('Q16-2', '#0055A4')
    st.write(color)
with col3:
    color = st.color_picker('Q16-3', '#DBDBDB')
    st.write(color)
with col4:
    color = st.color_picker('Q16-4', '#000347')
    st.write(color)
with col5:
    color = st.color_picker('Q16-5', '#B7F2FF')
    st.write(color)   


#!朝(morning)
df_morning = df[df['kwd'] == '朝(morning)']

df_morning_count = df_morning[['count',"col_sum"]].groupby("col_sum").count()

df_morning_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q17：朝(morning)")
st.bar_chart(df_morning_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q17-1', '#B7F2FF')
    st.write(color)
with col2:
    color = st.color_picker('Q17-2', '#E7FBFF')
    st.write(color)
with col3:
    color = st.color_picker('Q17-3', '#FFFFB5')
    st.write(color)
with col4:
    color = st.color_picker('Q17-4', '#FF2A22')
    st.write(color)
with col5:
    color = st.color_picker('Q17-5', '#FF9B56')
    st.write(color)   

    

#!昼(midday)
df_midday = df[df['kwd'] == '昼(midday)']

df_midday_count = df_midday[['count',"col_sum"]].groupby("col_sum").count()

df_midday_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q18：昼(midday)")
st.bar_chart(df_midday_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q18-1', '#FF9000')
    st.write(color)
with col2:
    color = st.color_picker('Q18-2', '#FFFF83')
    st.write(color)
with col3:
    color = st.color_picker('Q18-3', '#FF7F1A')
    st.write(color)
with col4:
    color = st.color_picker('Q18-4', '#FF6100')
    st.write(color)
with col5:
    color = st.color_picker('Q18-5', '#FFFF00')
    st.write(color)   


    
#!夕(sunset)
df_sunset = df[df['kwd'] == '夕(sunset)']

df_sunset_count = df_sunset[['count',"col_sum"]].groupby("col_sum").count()

df_sunset_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q19：夕(sunset)")
st.bar_chart(df_sunset_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q19-1', '#FF6100')
    st.write(color)
with col2:
    color = st.color_picker('Q19-2', '#D35000')
    st.write(color)
with col3:
    color = st.color_picker('Q19-3', '#FF9000')
    st.write(color)
with col4:
    color = st.color_picker('Q19-4', '#D37600')
    st.write(color)
with col5:
    color = st.color_picker('Q19-5', '#FFA511')
    st.write(color) 

    
    
#!夜(night)
df_night = df[df['kwd'] == '夜(night)']

df_night_count = df_night[['count',"col_sum"]].groupby("col_sum").count()

df_night_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

st.header("Q20：夜(night)")
st.bar_chart(df_night_count)

#streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
st.subheader("選択色トップ5")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    color = st.color_picker('Q20-1', '#000000')
    st.write(color)
with col2:
    color = st.color_picker('Q20-2', '#000347')
    st.write(color)
with col3:
    color = st.color_picker('Q20-3', '#000032')
    st.write(color)
with col4:
    color = st.color_picker('Q20-4', '#000276')
    st.write(color)
with col5:
    color = st.color_picker('Q20-5', '#FFFF00')
    st.write(color) 


