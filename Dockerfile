# syntax=docker/dockerfile:1
FROM python:3.7-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2-binary
RUN apk add build-base
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install python-dotenv
EXPOSE 5000
COPY . .
CMD ["flask", "run"]