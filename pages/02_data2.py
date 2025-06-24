import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 성동구 주요 행정동별 위도/경도 정보 (예시)
dong_locations = {
    "왕십리도선동": [37.5631, 127.0365],
    "마장동": [37.5663, 127.0414],
    "옥수동": [37.5469, 127.0155],
    "금호2.3가동": [37.5487, 127.0212],
    "행당1동": [37.5594, 127.0436],
    "행당2동": [37.5551, 127.0373],
    "성수1가제1동": [37.5454, 127.0551],
    "성수1가제2동": [37.5444, 127.0583],
    "성수2가제1동": [37.5415, 127.0507],
    "성수2가제3동": [37.5440, 127.0483],
    "금호1가동": [37.5473, 127.0275],
    "응봉동": [37.5601, 127.0342],
    "사근동": [37.5576, 127.0431],
}

# CSV 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("2024_2024_행정동별 세대주 성연령별 현황_연간.csv", encoding="euc-kr")
    df["2024년_거주자_총인구수"] = df["2024년_거주자_총인구수"].str.replace(",", "").astype(int)
    df = df[df["행정구역"].str.contains("성동구") & ~df["행정구역"].str.contains("성동구 \\(")]  # 전체 제외
    df["행정동"] = df["행정구역"].str.extract(r"성동구\s*(.*)\(")[0]
    df = df[["행정동", "2024년_거주자_총인구수"]]
    return df

# 데이터 로드
df = load_data()

# 지도 생성
m = folium.Map(location=[37.5636, 127.0365], zoom_start=13)

# 마커 추가
for _, row in df.iterrows():
    dong = row["행정동"]
    pop = row["2024년_거주자_총인구수"]
    coords = dong_locations.get(dong)
    if coords:
        folium.Marker(
            location=coords,
            popup=f"{dong}<br>총인구수: {pop:,}",
            tooltip=f"{dong} ({pop:,}명)",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

# Streamlit 앱
st.title("🗺 성동구 행정동별 인구 마커 지도")
st.markdown("성동구 주요 행정동의 총인구수를 **지도 위 마커**로 표시합니다.")
st.dataframe(df)  # 데이터 확인
st_folium(m, width=700, height=500)
