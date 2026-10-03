FROM python:3.14
WORKDIR /usr/svc/app
COPY inventory_manager.py, inventory.json .
CMD ["python", "inventory_manager.py"]