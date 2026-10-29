FROM python:3.14-slim
WORKDIR /usr/svc/app
COPY product.py main.py inventory.py file_handling.py inventory.json .
CMD ["python", "main.py"]