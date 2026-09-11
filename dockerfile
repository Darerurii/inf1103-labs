FROM python:3.14
WORKDIR /app
COPY auditor.py .
CMD ["python", "auditor.py"]