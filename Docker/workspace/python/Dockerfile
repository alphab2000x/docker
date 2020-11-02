FROM ubuntu

WORKDIR /usr/src/app
COPY . .
RUN apt-get -y update

RUN apt-get -y install python3 \
&& apt-get -y install python3-pip \
&& apt-get install -y git \
&& apt-get install -y vim \
&& pip3 install -r requirements.txt \
&& git config --global user.name barry \
&& git config --global user.email barrys.alpha@gmail.com \
&& git clone https://github.com/alphab2000x/docker.git

EXPOSE 8000