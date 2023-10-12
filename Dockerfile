FROM python:3.10.13-alpine3.17

COPY main.py /main.py
RUN chmod +x /main.py

ENTRYPOINT ["python","/main.py"]
