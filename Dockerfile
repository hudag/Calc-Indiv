FROM python:3.7

COPY . /web
WORKDIR /web
RUN pip install -r ./requirements.txt
ENTRYPOINT ["python"]

CMD ["/web/SQLite/sqlalchemy_insert.py"]