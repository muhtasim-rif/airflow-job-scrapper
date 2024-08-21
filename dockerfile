FROM apache/airflow:latest

USER root
RUN apt-get update &&\
    apt-get -y install git &&\
    apt-get clean

USER airflow
ENV PYTHONPATH="/opt/airflow"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt