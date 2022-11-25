FROM python:3.9.7

RUN mkdir app

COPY . .
WORKDIR /
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--reload"]