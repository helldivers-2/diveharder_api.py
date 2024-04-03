ARG PYVERSION=3.12.2
FROM python:${PYVERSION}-alpine

EXPOSE 1234

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/


CMD ["gunicorn", "diveharder.main:API", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:1234", "--log-syslog", "--log-level", "info"]
     


