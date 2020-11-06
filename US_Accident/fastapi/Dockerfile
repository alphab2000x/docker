FROM ubuntu

WORKDIR /usr/src/fastapi
COPY . .
RUN apt-get -y update

RUN apt-get -y install python3 \
&& apt-get -y install python3-pip \
&& apt-get install -y git \
&& apt-get install -y vim \
&& apt-get install -y nmap \
&& pip3 install -r requirements.txt 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]