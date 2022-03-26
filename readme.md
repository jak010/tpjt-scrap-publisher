# Django Template Repository

- Date: 2022.03.27

## TOC

- [README](#README)
- [Structure](#Structure)
- [Requirement](#Requirement)

### README

- 초기에 django project 생성 후 설정해야되는 부분을 template으로 만들고 가져다 쓰기 위해 생성함

### Structure

- `apps`
    - `apps` 디렉토리는 django의 app을 다루기 위해서 만듬
    - app 단위로 쪼개서 관리하는 방법이 제일 좋다고 하는데 필요하면 쪼개서 사용해도 상관 x
- `config`
    - django project 환경설정 파일
        - `setting`의 디렉토리에 `local`만 만들어 둠
            - `local` 에 포함된 내용
                - DATABASE
                - INSTALLED_APPS
                - ALLOWED_HOSTS
                - Internatinonalization 설정
                - LOGGING
    - `DATABASE`
        - `local.py`에 설정된 DATABASE 환경은 mysql을 기준으로 함
            - USERNAME: root
            - PASSWORD: 1234
            - DB_PORT: 9901
- `deployment`
    - 편의를 위한 docker-compose 포함됨
    - docker와 docker-compose가 설치된 환경에서 아래와 같이 사용하면 db 이용 가능
      ```sh
      $ cd deployment
      $ docker-compose up -d
      ```
- `runserver.sh`
    - 설명
      ```sh
      $ python manager.py runserver 0.0.0.0:8000 --settings=config.settings.local
      ```
        - 매번 위 명령어 치는 거 귀찮음으로 `runserver.sh` 만듬

### Requirement

- SQL LOGGING을 위한 `django-sqlformatters`가 포함되어 있음
- 그 외는 기본 `django` 포함 (3.2.10)

