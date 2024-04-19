FROM python:3.11.9-alpine

EXPOSE 1234

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apk update
RUN apk add git
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["gunicorn", "src.main:app", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:1234", "--log-syslog", "--log-level", "info"]
