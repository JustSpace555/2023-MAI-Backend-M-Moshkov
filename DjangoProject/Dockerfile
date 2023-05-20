FROM python:3.8

ENV DJANGO_SETTINGS_MODULE DjangoProject.settings_docker
RUN pip install --upgrade pip
WORKDIR /code
COPY . /code/
RUN ls -a
RUN pip install -r requirements.txt