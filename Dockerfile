FROM python:3.9.7

RUN mkdir app
ADD requirements.txt .
COPY . . 
WORKDIR /
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "app.main:app","--host=0.0.0.0","--reload"]