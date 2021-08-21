FROM python:3.7.3

COPY requirements.txt   requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

COPY ./app /shortlink/app
COPY ./bin /shortlink/bin
COPY wsgi.py /shortlink/wsgi.py
WORKDIR /shortlink

RUN useradd shortlink
RUN chown -R shortlink:shortlink /shortlink
RUN chmod 755 /shortlink
USER shortlink

EXPOSE 8080

ENTRYPOINT ["bash", "/shortlink/bin/run.sh"]