# 📊 인강 시청 패턴 분석을 통한 이탈 예측

안녕하세요!  
이 프로젝트는 **온라인 강의 시청 로그 데이터를 분석**하여  
수강자가 강의를 언제 중단(이탈)하는지를 예측하고,  
그 시청 패턴을 시각화하는 것을 목표로 합니다.

---

## 🔍 프로젝트 개요

- **주제**: 인강 시청 패턴 분석을 통한 이탈 예측  
- **목표**: 강의 시청 데이터를 바탕으로 이탈 지점을 분석하고 예측  
- **사용 데이터**: [Riiid EdNet KT3](https://github.com/riiid/ednet) (강의 시청 로그)  
- **분석 방식**: Python + Pandas + Matplotlib + Seaborn  

---

## 🛠️ 사용 기술

| 항목     | 내용                          |
|----------|-------------------------------|
| 언어     | Python 3                      |
| 분석 도구 | Pandas, NumPy                |
| 시각화   | Matplotlib, Seaborn           |
| 개발 환경 | PyCharm, Google Colab        |

---

## 🧱 폴더 구조

```
BigDataAnalysis/
├── data/                   # 원본 CSV 데이터 (ednet_kt3)
├── analysis/               # 분석 및 시각화 코드
│   ├── preprocess.py       # 전처리 함수
│   ├── visualize.py        # 시각화 함수
│   └── summary_report.ipynb # 분석 노트북
├── images/                 # 생성된 시각화 이미지
├── main.py                 # 분석 실행 스크립트
├── requirements.txt        # 의존 라이브러리 목록
└── README.md               # 프로젝트 개요
```

---

## 📈 주요 분석 항목

- 🎞 시청 비율 분포 분석 (video_watch_ratio)
- ⏰ 요일 및 시간대별 시청 활동 히트맵
- 📉 이탈 기준 정의 및 dropout 변수 생성
- 📊 강의 콘텐츠별 이탈 경향 시각화

---

## 📌 결과 요약

- 전체 사용자 중 약 60% 이상은 강의를 절반 이하만 시청
- 평일 오후~저녁 시간대에 시청 이탈 비율이 상대적으로 높음
- 일부 강의는 시작 몇 초 만에 이탈하는 패턴이 반복됨

---

## 📄 수행평가 제출물 구성

- `summary_report.ipynb`: 전체 분석 흐름 및 시각화 정리
- `README.md`: 프로젝트 설명 및 실행 정보

---

감사합니다! 😊