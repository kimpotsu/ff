import streamlit as st
import plotly.graph_objects as go

# 기본 설정
st.set_page_config(page_title="조승호 - 자기소개", layout="wide")

# 배경 이미지 스타일 추가
st.markdown("""
    <style>
    .main {
        background-image: linear-gradient(to right top, #e6f0ff, #f2fcff);
        background-attachment: fixed;
    }
    .value-box {
        background-color: rgba(255, 255, 255, 0.1);
        border-left: 6px solid #00c3ff;
        padding: 10px;
        margin: 10px 0;
        font-size: 16px;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #003366;
    }
    </style>
""", unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    st.markdown("### 🔥 조승호")
    st.caption("건양대학교 재난안전소방학과")
    st.caption("📌 좌우명: 긍정적인 사고를 갖자!")
    st.markdown("---")

    selected = st.radio("🧭 메뉴", ["인사 및 소개", "학업 배경", "경험 및 활동", "성격 및 특징", "미래 계획"])

    st.markdown("### 📊 전공 역량")
    skills = {
        "화재 안전": 85,
        "재난 대응": 78,
        "안전 관리": 92
    }
    for skill, value in skills.items():
        st.write(f"{skill} - {value}%")
        st.progress(value)

# 본문
st.title("🔥 조승호 자기소개")

if selected == "인사 및 소개":
    st.header("🙋‍♂️ 안녕하세요! 조승호입니다.")
    col1, col2, col3 = st.columns(3)
    col1.metric("이름", "조승호")
    col2.metric("학년", "학번: 21683029(3학년)")
    col3.metric("대학교", "건양대학교")

    st.subheader("재난안전소방학과 소개")
    st.info('"기사 자격증을 많이 취득해서 취업을 목표로 하겠습니다."')
    st.write("""
    안전한 사회를 만드는 것이 저의 사명입니다.  
    건양대학교 재난안전소방학과에서 화재 예방, 재난 대응, 안전 관리에 대한 전문 지식을 쌓고 있으며,  
    시민의 생명과 재산을 보호하는 전문가가 되기 위해 노력하고 있습니다.
    """)

    st.subheader("⚽ 나의 롤모델 - 손흥민 선수")
    st.write("""
    저는 **손흥민 선수**를 깊이 존경합니다.  
    그는 끊임없는 자기 관리와 노력, 팀을 위한 헌신적인 태도를 보여주는 진정한 프로입니다.  
    언제나 최선을 다하는 그의 모습은 제게 큰 동기부여가 됩니다.  
    소방공무원으로서 저도 같은 자세로 국민의 안전을 지키는 데 헌신하고 싶습니다.
    """)

    st.subheader("🎯 나의 취미")
    st.markdown("""
    <div style="display: flex; gap: 20px; flex-wrap: wrap;">
        <div style="flex:1; min-width:200px; background-color:#f0f8ff; padding:15px; border-radius:15px;">
            <h4>⚽ 축구</h4>
            <p>친구들과 주말마다 축구를 즐깁니다.<br> 팀워크와 체력 향상에 큰 도움이 됩니다.</p>
        </div>
        <div style="flex:1; min-width:200px; background-color:#fff0f5; padding:15px; border-radius:15px;">
            <h4>🏋️‍♂️ 헬스</h4>
            <p>매일 규칙적으로 헬스장에 다니며<br> 자기관리를 실천하고 있습니다.</p>
        </div>
        <div style="flex:1; min-width:200px; background-color:#f5fffa; padding:15px; border-radius:15px;">
            <h4>🧊 큐브 맞추기</h4>
            <p>두뇌 회전과 집중력 향상에 좋아서<br> 시간 날 때마다 즐기는 취미입니다.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif selected == "학업 배경":
    st.header("📚 학업 배경")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ 전공 선택 이유")
        st.markdown("""
        - 사회 안전에 기여하고 싶은 의지  
        - 재난 현장에서의 전문성 발휘  
        - 생명을 구하는 숭고한 직업에 대한 열망  
        - 과학적 접근을 통한 안전 시스템 구축  
        """)

        st.subheader("🎓 학력사항")
        st.markdown("""
        - **2021.03 ~ 현재**: 건양대학교 재난안전소방학과 (3학년 재학 중)  
        - **2018.03 ~ 2021.02**: 전북제일고등학교 졸업  
        - **2015.03 ~ 2018.02**: 이리영등중학교 졸업
        """)

    with col2:
        st.subheader("📘 주요 이수 과목")
        labels = ['소방전기', '소방기계', '산업안전', '위험물', '응급의학']
        values = [20, 18, 22, 15, 25]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 학업 성취도")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("평점 평균", "3.6")
    col2.metric("전공 이수 학점", "94")
    col3.metric("실습 과목 수", "12")
    col4.metric("프로젝트 참여", "5")

elif selected == "경험 및 활동":
    st.header("🧰 경험 및 활동")

    st.subheader("🚒 실습 및 현장 경험")
    st.markdown("""
    - **소방서 현장 실습 (2023.07)**: 논산소방서 3주간 실습, 화재 진압 및 구조 참관  
    - **재난 대응 시뮬레이션 (2023.09)**: 화재 및 지진 대응 훈련 참여
    """)

    st.subheader("🤝 동아리 및 봉사활동")
    st.markdown("""
    - **세이프가드 동아리 부회장**: 안전교육 프로그램 기획 및 운영  
    - **지역사회 봉사**: 화재 대피 교육, 누적 120시간
    """)

    st.subheader("📜 자격증 및 교육")
    col1, col2, col3 = st.columns(3)
    col1.success("소방 기계기사 준비 중")
    col2.info("토익 스피킹 준비")
    col3.warning("소방 전기기사 준비 중")

elif selected == "성격 및 특징":
    st.header("🧠 성격 및 특징")

    st.subheader("📊 핵심 역량 (레이더 차트)")
    labels = ['리더십', '책임감', '판단력', '협업능력', '전문성', '소통능력']
    values = [85, 95, 88, 92, 82, 87]

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=labels,
        fill='toself',
        name='역량 수준'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("💡 개인 강점")
    st.markdown("""
    - ❤️ **강한 책임감**: 맡은 일을 끝까지 완수  
    - ⚡ **신속한 판단력**: 위급 상황에서 빠른 판단  
    - 🤝 **협업 능력**: 원활한 소통과 협력  
    - 🎓 **지속적 학습**: 새로운 지식 습득 열정
    """)

    st.subheader("🌟 나의 가치관")
    st.markdown("""
    > "어떤 상황에서도 **긍정적인 태도**를 유지하려고 노력합니다.  
    > 어려움 속에서도 **배울 점을 찾고**, **성장 기회**로 삼는 것이 제 삶의 철학입니다."

    🔆 **긍정적인 사고**는 팀워크, 위기 대응, 인간관계에서 큰 힘이 됩니다.  
    소방공무원으로서 항상 밝고 유연한 자세로 시민과 동료에게 **안정감과 신뢰감을 주는** 사람이 되겠습니다.
    """)

elif selected == "미래 계획":
    st.header("🚀 미래 계획")

    st.subheader("📅 단계별 로드맵")
    st.markdown("""
    1. 🎓 졸업 준비 (2026년)  
    2. 📝 소방 전기,기계 자격증 (2025년)  
    3. 👨‍🚒 취업 후 근무 (2026년~)  
    4. 🧑‍🔬 전문가 도약 (2030년 이후)
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎯 단기 목표")
        st.markdown("""
        - 소방 전기,기계계 자격증 취득  
        - 자기소개서 작성  
        - 영어 토익 준비  
        - 컴활 자격증 준비
        """)

    with col2:
        st.subheader("🌄 장기 목표")
        st.markdown("""
        - 자격증 관련 취업  
        - 재난 대응 전문가로 성장  
        - 화재 예방 연구  
        - 지역사회 안전 기여
        """)

    st.subheader("❤️ 사회 기여 비전")
    st.info("""
    "안전한 사회를 만들어가는 것이 저의 궁극적인 목표입니다.  
    전문적인 지식과 기술을 바탕으로 시민의 생명과 재산을 보호하고,  
    재난 예방을 통해 더 나은 미래를 만들고자 합니다."
    """)


