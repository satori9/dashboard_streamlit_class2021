import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#日本語文字化け対策でフォント指定
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

        
#streamlitでの表示データのフィルタリング（まだ未装）
choose_id = st.selectbox("表示するIDを選択して下さい", (
        "ALL", "1"))
#choose_id = st.selectbox('Choose ID', df2, help = 'Filter report to show only one')    

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


