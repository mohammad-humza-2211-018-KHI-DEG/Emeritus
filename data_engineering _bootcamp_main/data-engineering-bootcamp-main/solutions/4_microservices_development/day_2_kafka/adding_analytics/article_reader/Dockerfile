FROM python:3.7
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -O /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY . /app/

WORKDIR /app
CMD bash -c "/wait-for-it.sh --timeout=0 broker:9092 -- gunicorn app:app -b 0.0.0.0:5000"