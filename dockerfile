FROM python:3.14
WORKDIR /usr/svc/app
COPY persistent_auditor.py .
CMD ["python", "persistent_auditor.py"]