FROM python:3.8

RUN apt-get update \
    && apt-get install -yyq netcat

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh ./entrypoint.sh

EXPOSE 8000

COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

ENTRYPOINT ["./entrypoint.sh"]
