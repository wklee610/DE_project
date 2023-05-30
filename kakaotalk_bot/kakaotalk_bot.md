#카카오톡 봇 만들기 (채용공고 offer)

채용공고에 대한 카카오톡 봇 만드는 목적
- - - 
채용공고를 놓치거나 or 링크드인과 같이 중복적으로 연락이 오는걸 방지하기 위한 목적
따라서 이미 있는 공고에 한해서는 따로 알림이 안오게 만드는 규칙을 선언해줄 예정

- 카카오톡 봇 언어 (python & Django)

- 나에게 필요한 서비스 (0 ~ 2년차 이하 개발자 / 데이터엔지니어 / 파이썬)
- 위치 서비스에 대한 지원은 X

진행 순서 (편집중)
- - - 
1. 크롤링으로 데이터 뽑기 (linkedin, jobkorea, saramin)
2. dataframe을 활용하여 csv 파일로 db에 input (db = mysql or mariadb)
3. Scheduler(Django or Airflow)를 활용하여 매일마다 새로운 데이터를 뽑아 데이터베이스에 넣기 (if data exists, pass)
4. kakao_bot에 연결
5. kakao_bot에서 기능 설정


