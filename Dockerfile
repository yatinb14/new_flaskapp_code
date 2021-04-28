#Docker FIle
FROM ubuntu
RUN apt-get update -y && apt-get install python3 python3-pip -y
RUN apt-get install default-libmysqlclient-dev -y
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
