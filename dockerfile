FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN  mkdir /providers-app
WORKDIR /providers-app
COPY . /providers-app
RUN pip install -r requirements/dev.txt
WORKDIR /providers-app/providers_server
RUN rm db.sqlite3
RUN python manage.py makemigrations && python manage.py migrate
RUN python manage.py loaddata fixture_data.json
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python" ,"manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

