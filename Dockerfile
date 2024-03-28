ARG PYVERSION=3.12.2
FROM python:${PYVERSION}

EXPOSE 1234

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./.env /code/.env
COPY ./diveharder /code/diveharder

CMD ["uvicorn", "diveharder.main:API", "--host", "0.0.0.0", "--port", "1234"]

