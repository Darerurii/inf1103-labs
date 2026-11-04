FROM python:3.14-slim
WORKDIR /usr/svc/app
COPY . ./
CMD ["python", "main.py"]