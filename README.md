# SKN24_EDA_MINI_6TEAM
---
## 🍦 TEAM I-스크림

**TEAM I-스크림**은  
모든 팀원이 MBTI `I`로 구성된 팀으로,  
조용하지만 집요하게 데이터를 파고드는 성향을 가지고 있습니다.

<!-- prettier-ignore-start -->
|김현수|류지우|조아름|진세형|최현진|
| :--: | :--: | :--: | :--: | :--: |
| [![github - BarryKim34](https://img.shields.io/badge/BarryKim34-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BarryKim34) | [![github - jia11234](https://img.shields.io/badge/jia11234-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jia11234) | [![github - areum117](https://img.shields.io/badge/areum117-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/areum117) | [![github - gugu_eightyone](https://img.shields.io/badge/gugu_eightyone-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gugu-eightyone) | [![github - lifeisgoodlg](https://img.shields.io/badge/lifeisgoodlg-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lifeisgoodlg) |
<!-- prettier-ignore-end -->

---
## 1. 프로젝트 개요
프로젝트 이름: **OST 오디오 특성 기반 영화 장르 예측 및 싱크 라이선싱 적합도 분석**

### 1-1. 프로젝트 소개
**"음악만 들어도 영화의 장르가 보일까?"**
이 프로젝트는 영화 OST의 오디오 데이터(Audio Features)를 분석하여 해당 곡이 어떤 장르의 영상에 적합한지 예측하는 머신러닝 모델을 구축하는 것을 목표로 합니다.

### 1-2. 프로젝트 목표
본 프로젝트는 단순한 장르 예측을 넘어, 음악 감독의 개인적 감각에 의존해 온 싱크 라이선싱(Sync Licensing) 프로세스의 비효율을 완화하고, 기존 발매곡(카탈로그 음악)의 잠재 가치를 재발견하는 것을 목표로 합니다.
- 장르 예측 모델 개발: 오디오 특성(Audio Features)만으로 해당 곡이 어떤 영화 장르(Action, Drama, Horror 등)에 속하는지 확률적으로 예측하는 머신러닝 모델 구축합니다.
- 장르 적합도 점수 도출: 예측된 확률값을 **장르 적합도 점수**로 활용하여 마케팅 타겟 설정 및 싱크 라이선싱 의사결정을 지원하는 보조 지표로 제안합니다.
---
## 2. 기술 스택

## 🛠 Tech Stack
| Category | Stack |
|----------|-------|
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **Crawling** | ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge&logo=python&logoColor=white) |
| **Data Processing** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) |
| **Machine Learning** | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white) ![XGBoost](https://img.shields.io/badge/XGBoost-EB5E28?style=for-the-badge) ![Optuna](https://img.shields.io/badge/Optuna-5A5A5A?style=for-the-badge) |
| **Visualization** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white) |
---

## 3. 데이터 수집

### 3-1. 오디오 특성 데이터 (Audio Features)
- Spotify 1 Million Tracks Dataset (Kaggle)
- 출처: https://www.kaggle.com/datasets/amitanshjoshi/spotify-1million-tracks
- 설명:
    - Spotify에서 제공하는 Audio Features 기반 데이터
    - danceability, energy, valence, tempo 등 곡의 음향적 특성을 수치화한 변수 포함
- 목적: 영화 OST의 음악적 무드를 정량적으로 표현하는 입력 데이터로 활용

### 3-2. 영화 메타데이터 (Movie Metadata)
- The Movies Dataset (Kaggle)
- 출처: https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv
- 설명: 영화 제목, 장르 등 기본 메타정보 포함
- 목적: 영화 장르 정의

### 3-3. 영화 OST 데이터 (Soundtrack Collection)
- IMDb (Web Crawling)
- 출처: IMDb ID(imdb_id)를 기준으로 영화별 OST 정보 크롤링
- 설명: 영화 리스트 데이터의 IMDb ID를 활용하여 각 영화의 공식 사운드트랙 정보 수집
- 목적: 영화와 Spotify 트랙을 연결하는 매핑 테이블 생성

## 4. 데이터 전처리 및 통합

### 4-1. 원본 데이터 구조 및 전처리 과정
#### 영화 메타데이터
- 원본 데이터
<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/559223ed-e955-43f2-8c4d-b4ae7d9023d9" />

- 불필요 컬럼 제거
<img width="405" height="311" alt="image" src="https://github.com/user-attachments/assets/e3ba0f2d-022e-417d-adff-9889a431fb6c" />
<img width="1338" height="195" alt="image" src="https://github.com/user-attachments/assets/3b0900fe-743b-4566-93a4-5320dc2713b8" />


### 사운드트랙 리스트
<img width="356" height="280" alt="image" src="https://github.com/user-attachments/assets/a1632610-85aa-460a-b5b4-4f9342fafc7f" />  
<img width="555" height="162" alt="image" src="https://github.com/user-attachments/assets/d516c2d2-2aab-4ad9-8406-1ebe42a6674a" />


#### 오디오 특성 데이터
<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/479e9ab4-1853-449a-a8fb-682eb254c5d2" />

- 중복값 확인
<img width="616" height="438" alt="image" src="https://github.com/user-attachments/assets/49a05d87-271a-4507-820a-81ba32219fb8" />


### 4-2. 통합 데이터
<img width="359" height="495" alt="image" src="https://github.com/user-attachments/assets/c8c03166-185f-421c-8806-de6dfc098158" />
<img width="377" height="383" alt="image" src="https://github.com/user-attachments/assets/2e618a31-25a3-460c-a302-1f4632a21145" />


## 5. 데이터 분석
### 주요 장르별 오디오 특성 패턴 비교 (Line Plot)
<img width="1390" height="690" alt="image" src="https://github.com/user-attachments/assets/1b695b75-6979-43e4-9f9e-dc769c403be9" />
위 그래프는 데이터 수가 많은 상위 6개 장르(Action, Romance, Horror, Drama, Comedy, Sciencce Fiction)를 대상으로 패턴을 선 그래프로 비교한 결과입니다.

- energy: Action / Horror / S.F. / Comedy vs. Romance / Drama
- acousticness: Romancce / Drama에서 상대적으로 높게 나타남 -> 감정 전달 중심의 음악적 특성이 나타남
- 영화 장르에 따라 패턴의 차이는 있지만, 그 정도가 크지 않은 형태를 보임.

## 6. 모델 설계 및 학습
본 프로젝트에서는 음악적 특성(danceability, energy, loudness, acousticness, valence, tempo)을 기반으로 학습하였으며</br>
주요 모델로 **랜덤 포레스트(Random Forest)** 를 선택함
```python
rf_clf = RandomForestClassifier(
    max_depth=20,           
    n_estimators=500,      
    max_features='sqrt', 
    random_state=42,
    class_weight='balanced' # 소수 클래스에 가중치 부여
)
```
## 7. 모델 평가
클래스별 확률 출력에서 상위 N개 클래스를 선택하여 다중 클래스 예측 수행
```python
# 2차원 빈 배열 생성 (0으로 초기화)
y_pred = np.zeros_like(proba_df.values)

for i in range(len(proba_df)):
    # 확률을 오름차순 정렬한 후 상위 N개 클래스의 인덱스 선택
    top_n_idx = np.argsort(proba_df.iloc[i].values)[-N:]
    y_pred[i, top_n_idx] = 1

return y_pred
```
위를 활용하여 F1_score 평가함</br>
상위 3개의 클래스를 후보로 선택 했을 떄 42% 정확도를 보임
```
Top-1 | Micro F1: 0.321 | Macro F1: 0.097
Top-2 | Micro F1: 0.413 | Macro F1: 0.159 
Top-3 | Micro F1: 0.422 | Macro F1: 0.191 
Top-5 | Micro F1: 0.401 | Macro F1: 0.213 
```
- Micro F1: 전체 샘플 기준 정확도 (샘플 수가 많은 클래스 영향)
- Macro F1: 각 클래스 평균 F1 (소수 클래스 성능 반영)

## 8. 실험 결과 및 분석
### MUSIC, ACTION 장르에 편향되는 경향있다.
### 샘플 10009번 노래 제목: Sidetrack
<img width="907" height="547" alt="image" src="https://github.com/user-attachments/assets/22b378e9-62a0-42b7-b7dd-b3809968a881" /> </br>
### 샘플 209555번 노래 제목: Only 1
<img width="907" height="547" alt="image" src="https://github.com/user-attachments/assets/5aa82921-e80b-43d8-a3c0-0e6a08fee080" /> </br>
### 샘플 1355번 노래 제목: XNXX
<img width="907" height="547" alt="image" src="https://github.com/user-attachments/assets/baf69ae0-3e2d-4b85-8b24-70a165d296ee" /> </br> 

## 9. 한계점 및 개선 방향
### 9-1. 장르 라벨의 본질적 모호성
- Drama, Comedy, Romance와 같이 감정 스펙트럼이 넓고 장르 간 경계가 모호한 경우, 오디오 특성만으로 명확한 분리가 어려운 모습을 보였습니다.
### 9-2. 장르 불균형 문제
- Drama, Comedy: 데이터 수가 매우 많음
- War, Western, TV Movie: 상대적으로 데이터 수가 부족함
이로 인해 일부 장르의 ROC-AUC는 일정 수준을 달성하였으나, 실제 예측 성능을 반영하는 F1-score가 낮게 측정되는 현상이 발생하였습니다.
### 9-3. 개선 방향
향후 다음과 같은 데이터가 결합될 경우, 예측 성능 및 해석력이 크게 향상될 것이라 기대됩니다.
- OST 사용 장면 정보 (트레일러 / 엔딩 / 하이라이트)
- 가사(Lyrics) 기반 감성 분석
- 텍스트 메타데이터(영화 시놉시스, 키워드)
---
## 회고록
- `김현수`</br>

- `류지우` 여러 머신러닝 모델을 직접 구현하고 실험해보면서 이론으로만 이해하던 내용을 실제로 체감할 수 있었습니다. 특히 랜덤 포레스트 모델을 집중적으로 다루며 학습 파라미터를 조정해 원하는 결과를 얻는 과정을 경험하면서 모델 학습 효율을 높이는 방법을 익혔습니다. 하지만 기대한 성과가 나오지 않아 아쉬움이 남았고 더 많은 데이터 수집과 전처리가 필요하다고 생각했습니다.</br>

- `조아름`</br>
 
- `진세형` 주요 전처리 과정을 수행할 수 있어서 의미있었습니다. 다만, 문제점 하나를 해결하면 다른 부분에서 문제점이 발견되곤 했었는데, 전처리를 종합적으로 계획할 필요가 있어보입니다. 더불어, ML과정에서 한 모델에 치중하지 말고, 다양한 모델을 활용해야 하겠습니다.</br>
  
- `최현진` 이전에는 예쁘게 잘 만들어진 데이터셋을 활용하여 머신러닝을 돌렸지만, 이번 프로젝트를 통해서 직접 수집한 데이터를 활용해 머신러닝을 돌릴 수 있어서 흥미로웠습니다. 다만, 데이터의 불균형이 심해 모델을 학습해도 만족스러운 유의미한 결과를 바로 얻지 못한 것이 아쉽습니다. 때문에 모델을 학습하기 이전에 데이터를 어떻게 전처리하고 다뤄야 하는지를 더 학습해야겠다는 생각이 들었습니다.이전에는 예쁘게 잘 만들어진 데이터셋을 활용하여 머신러닝을 돌렸지만, 이번 프로젝트를 통해서 직접 수집한 데이터를 활용해 머신러닝을 돌릴 수 있어서 흥미로웠습니다. 다만, 데이터의 불균형이 심해 모델을 학습해도 만족스러운 유의미한 결과를 바로 얻지 못한 것이 아쉽습니다. 때문에 모델을 학습하기 이전에 데이터를 어떻게 전처리하고 다뤄야 하는지를 더 학습해야겠다는 생각이 들었습니다.</br>

