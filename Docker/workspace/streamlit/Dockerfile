FROM ubuntu

WORKDIR /usr/src/app
COPY . .
RUN apt-get -y update

RUN apt-get -y install python3 \
&& apt-get -y install python3-pip \
&& apt-get install -y git \
&& apt-get install -y vim \
&& pip3 install -r requirements.txt 

# CMD ["python", "algo.py"]
CMD ["streamlit", "run", "streamlit.py"]