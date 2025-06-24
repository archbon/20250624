
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv("2024_2024_행정동별 세대주 성연령별 현황_연간.csv", encoding="euc-kr")
    df["2024년_거주자_총인구수"] = df["2024년_거주자_총인구수"].str.replace(",", "").astype(int)
    df = df[df["행정구역"].str.contains("성동구") & ~df["행정구역"].str.contains("성동구 \\(")]  # 전체 성동구 제외
    df["행정동"] = df["행정구역"].str.extract(r"성동구\s*(.*)\(")[0]
    return df[["행정동", "2024년_거주자_총인구수"]]

# GeoJSON 로드
@st.cache_data
def load_geojson():
    import json
    with open("seongdong_dong.geojson", encoding='utf-8') as f:
        geo = json.load(f)
    return geo

# 데이터 불러오기
df = load_data()
geojson = load_geojson()

st.title("🗺 2024년 성동구 행정동별 인구 지도 시각화")
st.markdown("행정동별 총인구수를 **지도 위 색상으로 시각화**합니다.")

# folium 지도 생성
m = folium.Map(location=[37.5636, 127.0365], zoom_start=13)

# 인구 수로 색상 구분
choropleth = folium.Choropleth(
    geo_data=geojson,
    data=df,
    columns=["행정동", "2024년_거주자_총인구수"],
    key_on="feature.properties.name",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.3,
    legend_name="총인구수",
).add_to(m)

# 각 지역에 팝업 추가
for feature in geojson["features"]:
    dong_name = feature["properties"]["name"]
    population = df[df["행정동"] == dong_name]["2024년_거주자_총인구수"].values
    popup_text = f"{dong_name}<br>총인구수: {population[0]:,}" if len(population) > 0 else dong_name
    folium.Popup(popup_text).add_to(folium.GeoJsonTooltip(fields=["name"]).add_to(m))

# 스트림릿에 지도 표시
st_folium(m, width=700, height=500)
