FROM python:3.10
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /app/
EXPOSE 8000
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]

