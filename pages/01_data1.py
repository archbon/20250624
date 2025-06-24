import streamlit as st
import pandas as pd

# CSV 파일 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("2024_2024_행정동별 세대주 성연령별 현황_연간.csv", encoding='euc-kr')
    df["2024년_거주자_총인구수"] = df["2024년_거주자_총인구수"].str.replace(",", "").astype(int)
    return df

df = load_data()

st.title("📊 2024년 성동구 행정동별 연령대별 인구현황")
st.markdown("총인구수를 기준으로 상위 5개 행정동의 연령대별 인구 분포를 선 그래프로 나타냅니다.")

# 원본 데이터 표시
st.subheader("🗂 원본 데이터 (일부)")
st.dataframe(df.head(10))

# 상위 5개 행정동 선별
top5_df = df.nlargest(5, "2024년_거주자_총인구수")

# 분석에 사용할 컬럼 추출
age_columns = [col for col in df.columns if col.startswith("2024년_거주자_") and "총인구수" not in col]
clean_age_columns = [col.replace("2024년_거주자_", "") for col in age_columns]

# 나이대별 인구수로 구성된 데이터프레임 생성
age_data = top5_df[age_columns].copy()
age_data.columns = clean_age_columns
age_data.index = top5_df["행정구역"]
age_data = age_data.transpose()

# 선 그래프 시각화
st.subheader("📈 연령대별 인구 분포 (상위 5개 행정동)")
st.line_chart(age_data)
