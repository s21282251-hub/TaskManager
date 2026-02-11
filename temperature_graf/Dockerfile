FROM python:slim

WORKDIR /project

COPY ./requirements.txt /project/requirements.txt
COPY ./.env /project

RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt

COPY ./app /project/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]