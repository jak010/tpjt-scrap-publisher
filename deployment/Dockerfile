FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=1234

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
RUN apt update
RUN apt install -y wget unzip

WORKDIR /

# 초기 데이터베이스 환경 구성 시 필요함
ADD init-db.sh /docker-entrypoint-initdb.d

CMD ["mysqld"]