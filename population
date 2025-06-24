import pandas as pd
import streamlit as st

# 📁 CSV 파일 불러오기 (EUC-KR 인코딩)
@st.cache_data
def load_data():
    df = pd.read_csv("202505_202505_연령별인구현황_월간.csv", encoding="euc-kr")
    df["2025년05월_계_총인구수"] = df["2025년05월_계_총인구수"].str.replace(",", "").astype(int)
    top5 = df.nlargest(5, "2025년05월_계_총인구수").copy()

    age_columns = [col for col in top5.columns if col.startswith("2025년05월_계_") and "세" in col]
    new_col_names = [col.split("_")[-1].replace("세", "").replace(" ", "").replace("이상", "100+") for col in age_columns]

    age_df = top5[age_columns].copy()
    age_df.columns = new_col_names
    age_df.insert(0, "행정구역", top5["행정구역"])
    age_df.insert(1, "총인구수", top5["2025년05월_계_총인구수"])

    return age_df

# 📊 데이터 불러오기
df = load_data()

# 🧾 앱 제목
st.set_page_config(page_title="2025년 인구 현황", layout="wide")
st.title("📊 2025년 5월 기준 상위 5개 행정구역 연령별 인구 현황")

st.markdown("""
이 웹앱은 2025년 5월 기준 **총인구수 상위 5개 지역**의  
연령별 인구 분포를 선그래프로 시각화합니다.  
*단위: 명*
""")

# 🖥 원본 데이터 표시
st.subheader("📋 상위 5개 행정구역 연령별 인구 데이터")
st.dataframe(df, use_container_width=True)

# 📈 선 그래프용 데이터 가공
plot_df = df.drop(columns=["총인구수"]).set_index("행정구역")
plot_df = plot_df.applymap(lambda x: int(str(x).replace(",", "")))  # 숫자형 변환
plot_df = plot_df.T  # 연령을 인덱스로

# 📉 선그래프 출력
st.subheader("📈 연령별 인구 변화 그래프")
st.line_chart(plot_df)
