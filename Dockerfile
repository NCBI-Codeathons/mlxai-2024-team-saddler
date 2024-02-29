FROM python:3.11

ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /usr/src

RUN apt update && apt install -y vim wget openjdk-17-jdk

RUN git clone https://github.com/NCBI-Codeathons/mlxai-2024-team-saddler.git

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install wheel setuptools build
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/blackadad/paper-scraper.git

RUN rm -rf /home/root/.cache

# CMD add here command to automatically lunch interface when available