FROM apache/airflow:latest

USER root
RUN apt-get update &&\
    apt-get -y install git &&\
    apt-get clean

USER airflow
ENV PYTHONPATH="/opt/airflow"
ENV SERPAPI_API_KEY=65a170ad84895c39a99003aa0f033fe7def1f0c7

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt