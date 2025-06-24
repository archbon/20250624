import streamlit as st

# 페이지 제목
st.title("MBTI 기반 직업 추천 서비스")

# 설명
st.markdown("""
안녕하세요! 👋  
아래에서 본인의 MBTI 성격 유형을 선택하면,  
해당 성향에 어울리는 추천 직업을 알려드릴게요!
""")

# MBTI 유형 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# MBTI 직업 추천 매핑
mbti_careers = {
    "INTJ": ["데이터 과학자", "전략 컨설턴트", "AI 개발자", "시스템 설계자"],
    "INTP": ["연구원", "이론 물리학자", "프로그래머", "UX 디자이너"],
    "ENTJ": ["경영 컨설턴트", "CEO", "프로젝트 매니저", "변호사"],
    "ENTP": ["창업가", "마케팅 전문가", "기술 분석가", "스타트업 기획자"],
    "INFJ": ["심리상담가", "교사", "작가", "HR 전문가"],
    "INFP": ["작가", "예술가", "콘텐츠 크리에이터", "사회복지사"],
    "ENFJ": ["교육자", "조직 리더", "브랜드 매니저", "코치"],
    "ENFP": ["기획자", "여행 작가", "마케터", "콘텐츠 제작자"],
    "ISTJ": ["공무원", "회계사", "데이터 분석가", "품질 관리자"],
    "ISFJ": ["간호사", "사회복지사", "관리자", "고객지원"],
    "ESTJ": ["기업 관리자", "군인", "운영 책임자", "회계 감사"],
    "ESFJ": ["교사", "간호사", "인사 담당자", "세일즈"],
    "ISTP": ["엔지니어", "기술 분석가", "자동차 정비사", "보안 전문가"],
    "ISFP": ["패션 디자이너", "사진작가", "요리사", "물리치료사"],
    "ESTP": ["영업 전문가", "응급 구조사", "이벤트 기획자", "스포츠 코치"],
    "ESFP": ["배우", "가수", "퍼포먼스 아티스트", "여행가이드"]
}

# 사용자 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 👇", mbti_types)

# 결과 출력
if selected_mbti:
    st.subheader(f"🧭 {selected_mbti} 유형에게 어울리는 직업:")
    for job in mbti_careers[selected_mbti]:
        st.write(f"• {job}")
