FROM python:3.9-slim-buster
COPY ./requirements.txt /app
COPY . .
EXPOSE 5000
ENV FLASK_APP=my_flask.py
CMD ["flask", "run", "--host", "0.0.0.0"]