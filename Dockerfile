FROM python:3.7-alpine
WORKDIR . /app
COPY ./code.py /app
ENTRYPOINT [ "python" ]
CMD [ "code.py" ]
