FROM python:3.7-alpine
RUN pip install flask
WORKDIR /app
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "code.py" ]
