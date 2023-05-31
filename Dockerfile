FROM python:3.11-slim

RUN useradd -ms /bin/bash ngp
USER ngp
WORKDIR /home/ngp

COPY ./requirements.txt requirements.txt

USER root
RUN apt-get update \
    && pip3 install -r requirements.txt
USER ngp

COPY ./src /home/ngp/

CMD ["python3", "main.py"]