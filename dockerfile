FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN  mkdir /providers-app
WORKDIR /providers-app
COPY . /providers-app
RUN pip install -r requirements.txt
WORKDIR /providers-app/providers_server
RUN python manage.py makemigrations && python manage.py migrate
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python" ,"manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

