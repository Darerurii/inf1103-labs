FROM python:3.14
WORKDIR /app
COPY auditor.py .
CMD ["python", "modular_auditor.py"]